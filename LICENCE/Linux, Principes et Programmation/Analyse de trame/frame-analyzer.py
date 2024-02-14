# Importation des modules nécessaires
import socket
import logging
import struct
import psycopg2
import json
from psycopg2 import sql

# Configuration du logging pour afficher les informations
# Les informations seront stockées dans le fichier 'network_traffic.log'
logging.basicConfig(filename='network_traffic.log', level=logging.INFO)

# Paramètres de connexion à la base de données
# Ces informations sont nécessaires pour se connecter à la base de données PostgreSQL
db_config = {
    'host': 'localhost',
    'database': 'network_traffic',
    'user': 'postgres',
    'password': 'root'
}


# Connexion à la base de données
# Nous utilisons les paramètres définis ci-dessus pour établir la connexion
conn = psycopg2.connect(**db_config)
cur = conn.cursor()

# Création de la table si elle n'existe pas
# Cette table stockera les informations sur le trafic réseau
cur.execute("""
    CREATE TABLE IF NOT EXISTS network_traffic (
        id SERIAL PRIMARY KEY,
        info JSONB
    )
""")
conn.commit()


# Dictionnaire pour mapper les valeurs Ethertype à leurs noms correspondants
# Ethertype est un champ dans un cadre Ethernet qui indique quel protocole est encapsulé dans la charge utile du cadre
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
# Cette fonction prend les données brutes d'un paquet Ethernet et extrait les adresses MAC de destination et source et l'Ethertype
def ethernet_header(raw_data):
    dest_mac, src_mac, ethertype = struct.unpack('! 6s 6s H', raw_data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), ETHERTYPE_MAP.get(ethertype, f'Unknown (0x{ethertype:04x})')

# Fonction pour convertir une adresse MAC en bytes en une adresse MAC lisible
# Cette fonction prend une adresse MAC en bytes et la convertit en une chaîne de caractères lisible
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

# Fonction pour stocker les informations capturées dans la base de données
# Cette fonction prend un dictionnaire d'informations, le convertit en une chaîne JSON, et l'insère dans la base de données
def store_in_db(info):
    info['tram'] = info['tram'].replace('\0', '')
    info_str = json.dumps(info)
    logging.info(info_str)
    cur.execute(
        sql.SQL("INSERT INTO network_traffic (info) VALUES (%s)"),
        [info_str]
    )
    conn.commit()

    
# Fonction principale
# Cette fonction crée un socket pour écouter les paquets Ethernet, les décode, et stocke les informations dans la base de données
def main():
    host = 'enp0s3'
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    s.bind((host, 0))
    print(f"Écoute sur {host} ...")
    print("Appuyez sur Ctrl-C pour arrêter.")
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