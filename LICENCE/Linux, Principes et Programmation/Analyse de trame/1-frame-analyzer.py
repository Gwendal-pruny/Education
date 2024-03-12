import socket
import logging
import struct
import json
import mysql.connector


# Configuration du logging
logging.basicConfig(
  filename='network_traffic.log',
  level=logging.INFO,
  format='%(message)s',
)

# Paramètres de connexion à la base de données
db_config = {
    'host': 'localhost',
    'database': 'network',
    'user': 'admin',
    'password': 'admin'
}

# Dictionnaire pour mapper les valeurs Ethertype à leurs noms correspondants
ETHERTYPE_MAP = {
    0x0800: 'Internet Protocol version 4 (IPv4)',
    0x86DD: 'Internet Protocol Version 6 (IPv6)',
    0x0806: 'Address Resolution Protocol (ARP)',
    0x0842: 'Wake-on-LAN',
    0x22F3: 'IETF TRILL Protocol',
    0x6003: 'DECnet Phase IV',
    0x8035: 'Reverse Address Resolution Protocol',
    0x809B: 'AppleTalk (Ethertalk)',
    0x80F3: 'AppleTalk Address Resolution Protocol (AARP)',
    0x8100: 'VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq[4]',
    # Ajoutez d'autres valeurs Ethertype ici au besoin
}

# Fonction pour décoder l'en-tête Ethernet
def ethernet_header(raw_data):
    dest_mac, src_mac, ethertype = struct.unpack('! 6s 6s H', raw_data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), ETHERTYPE_MAP.get(ethertype, f'Unknown (0x{ethertype:04x})')

# Fonction pour convertir une adresse MAC en bytes en une adresse MAC lisible
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

# Fonction pour stocker les informations capturées dans la base de données
def store_in_db(info):
    # Connexion à la base de données
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()

    # Insertion des données dans la base de données
    query = "INSERT INTO network_traffic (tram, dest_mac, src_mac, ethertype) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (info['tram'], info['dest_mac'], info['src_mac'], info['ethertype']))

    # Commit des changements et fermeture de la connexion
    conn.commit()
    cur.close()
    conn.close()
# Fonction principale
def main():
    host = 'enp0s3'
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    s.bind((host, 0))
    print(f"Écoute sur {host} ...")
    print("Appuyez sur Ctrl-C pour arrêter.")
    
    # Ajout d'un compteur de trames
    nb_trames = 0

    while True:
        raw_data, addr = s.recvfrom(65565)
        logging.info(f"Trame : {raw_data}")
        dest_mac, src_mac, ethertype = ethernet_header(raw_data)
        logging.info(f"Destination MAC: {dest_mac}, Source MAC: {src_mac}, Ethertype: {ethertype}")
        info = {
            'tram': raw_data.decode('utf-8', 'ignore'),
            'dest_mac': dest_mac,
            'src_mac': src_mac,
            'ethertype': ethertype
        }
        store_in_db(info)

# Exécution de la fonction principale si le script est exécuté directement
if __name__ == '__main__':
    main()
