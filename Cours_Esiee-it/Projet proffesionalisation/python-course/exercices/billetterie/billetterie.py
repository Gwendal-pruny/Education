"""
Cours "Introduction 1" - Exercice "Billetterie"
"""

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
nb_billets_adulte = 0
nb_billets_reduice = 0
has_reduit = False
station_start_name = None
station_end_name = None
distance = 0
voie = 1



# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

# Questions à l'utilisateur
print("\n--- Combien souhaitez-vous de billets à tarif plein ?")
nb_billets_adulte = int(input("Billets : "))

print("\n--- Souhaitez-vous des billets à tarif réduit ? oui / non")
has_reduit = str(input("oui / non : "))

if has_reduit != False and has_reduit != "non" :
    print("\n--- Combien des billets à tarif réduit souhaitez-vous ?")
    nb_billets_reduice = int(input("Billets : "))



print("////////////////// Liste des stations disponibles //////////////////")
print("\nQuelle est votre station de départ ? (Indiquer le nombre associer a la gare)")
print("0.Meinohama, 1.Muromi, 2.Fujisaki, 3.Nishijin, 4.Tojinmachi, 5.Ohorikoen (Ohori Park)")
print("6.Akasaka, 7.Tenjin, 8.Nakasu-Kawabata, 9.Gion, 10.Hakata, 11.Higashi-Hie, 12.Fukuokakuko(Airport)")
print("////////////////// ////////////////// //////////////////")
station_start = int(input(" Choix numéro : "))
station_start_name = (stations_names[station_start])
print("Départ : ")
print(station_start_name)

print("////////////////// Liste des stations disponibles //////////////////")
print("\nQuelle est votre station de d'arriver ? (Indiquer le nombre associer a la gare)")
print("0.Meinohama, 1.Muromi, 2.Fujisaki, 3.Nishijin, 4.Tojinmachi, 5.Ohorikoen (Ohori Park)")
print("6.Akasaka, 7.Tenjin, 8.Nakasu-Kawabata, 9.Gion, 10.Hakata, 11.Higashi-Hie, 12.Fukuokakuko(Airport)")
print("////////////////// ////////////////// //////////////////")
station_end = int(input("Choix numéro : "))
station_end_name = (stations_names[station_end])
print("Arriver : ")
print(station_end_name)

if stations_names[station_start:station_end] == [] :
    if stations_names[station_end:station_start] == [] :
        print("INVALIDE TRY AGAIN")
    else :
        voie = 2


print("////////////////////////// ITINERAIRE //////////////////////////")
print("Itinéraire : ")
if voie == 2 :
    print(stations_names[station_end:station_start])
    print("reversed")
else :
    print(stations_names[station_start:station_end])
    voie = 1
print("//////////////////////////////////////////////////////////////// ")


# Calculs de l'itinéraire
print("////////////////////////// DISTANCE //////////////////////////")
if voie == 2 :
    distance = sum(stations_distances[station_end:station_start])
else :
    distance = sum(stations_distances[station_start:station_end])
print("Vous allez parcourir")
print(distance)
print("kilomètres")
print("//////////////////////////////////////////////////////////////")


# Choix de la bonne zone tarifaire

if distance <= 3:
    tarif = 210
if distance >= 3.1:
    tarif = 270
if distance >= 7.1:
    tarif = 300
if distance >= 11.1:
    tarif = 340



# Calcul du coût total

Prix = ((nb_billets_adulte * tarif)+(nb_billets_reduice * (tarif / 2)))


# Affichage des détails du voyage et du tarif
# Affichage de la voie du train à emprunter

print("//////////////////////////////////////////////////////////////")
print("Itinéraire :")
if voie == 2 :
    print(stations_names[station_end:station_start])
else :
    print(stations_names[station_start:station_end])
print("Distance a parcourir :")
print(distance)
print("Le montant a payer est de :")
print(Prix)
print("Votre train est sure la voix : \n Merci de votre achat et Bon voyage !")
print(voie)
print("//////////////////////////////////////////////////////////////")
