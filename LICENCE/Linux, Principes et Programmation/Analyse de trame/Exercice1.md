

Linux - Principes et Programmation

Exercice #1

Création d'un Analyseur de trames réseau.

A l'aide du script fourni :

implémenter les fonctionnalités suivantes en le complétant



import socket
def main():
   host = 'enp0s3'
   s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
   s.bind((host, 0))
   p = 0
   while True:
       data = s.recvfrom(65565)
       p += 1
       print(data)
 
if __name__ == '__main__':
   main()


La description de l'entête Ethernet peut être trouvée sur : https://www.frameip.com/entete-ethernet/

Vous utiliserez l'entête de 14 octets.

1) Afficher seulement les entêtes Ethernet

2) Afficher ces mêmes entêtes en utilisant la bibliothèque "logging" (https://docs.python.org/3/library/logging.html)

3) décoder tous les champs de l'entête Ethernet et les afficher (toujours sous forme de logs). Vous pourrez utiliser la bibliothèque "struct" de Python.

31 janvier 2024 - Seconde partie

Le but de cette seconde partie est de construire le POC d'un outil qui pourrait déboucher sur un analyseur de trafic et de visualisation des information collectées.

1) Le script précédent doit maintenant intégrer une fonctionnalité permettant analyser tous les champs des entêtes IPv4, IPv6, ARP , ICMPv4, TCP et UDP.

2) Les informations capturées seront dans un premier enregistrées dans un fichier texte, au format généré par la bibliothèque "logging".

3) Dans un second temps, les informations seront stockées dans une des bases de données suivante : InfluxDB, PostgreSQL, MariaDB ou MySql.

Pour cette seconde partie, extension de la première, vous pourrez travailler par groupes de deux personnes maximum.

Dans ce cas, les participants pourront héberger la base de données sur un second PC/Machine virtuelle.

12 février 2024 -Troisième partie

Les données stockées dans la base de données retenue seront exploitées graphiquement à l'aide de l'outil Grafana (https://grafana.com/oss/grafana/) qui permet de créer des tableaux de bord.

Votre rapport sera transmis par mail au plus tard à 15h00 le lundi 12 février 2024 à mail@thierry-decker.com.

L'objet du mail sera : [L3 Linux, principes et programmation 2024]