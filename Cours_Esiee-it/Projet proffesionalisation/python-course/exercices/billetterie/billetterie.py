"""
Cours "Introduction 1" - Exercice "Billetterie"
"""
#Import
from simple_term_menu import TerminalMenu

# Déclaration de toute les variables utiliser
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
conditionGare = True
conditionBillet = True

# escape sequences
print(chr(27) + "[2J")

# Introduction
print("・．━━━━━━━━━━━━━━━━━━━━━ † ━━━━━━━━━━━━━━━━━━━━━．・")
print("          ╭━━━┳╮╱╭┳╮╭━┳╮╱╭┳━━━┳╮╭━┳━━━╮")
print("          ┃╭━━┫┃╱┃┃┃┃╭┫┃╱┃┃╭━╮┃┃┃╭┫╭━╮┃")
print("          ┃╰━━┫┃╱┃┃╰╯╯┃┃╱┃┃┃╱┃┃╰╯╯┃┃╱┃┃")
print("          ┃╭━━┫┃╱┃┃╭╮┃┃┃╱┃┃┃╱┃┃╭╮┃┃╰━╯┃")
print("          ┃┃╱╱┃╰━╯┃┃┃╰┫╰━╯┃╰━╯┃┃┃╰┫╭━╮┃")
print("          ╰╯╱╱╰━━━┻╯╰━┻━━━┻━━━┻╯╰━┻╯╱╰╯")

print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")


# Questions des billets à l'utilisateur
while True :
    print("\n-> Combien souhaitez-vous de billets à tarif plein ?")
    terminal_menu = TerminalMenu(["0","1","2","3","4","Choisire le nombre"])
    nb_billets_adulte = terminal_menu.show()
    if nb_billets_adulte == 5 :
        try:
            nb_billets_adulte = int(input("Nombre de billets :"))
            break
        except ValueError:
            print(chr(27) + "[2J")
            print("Merci d'utiliser des nombre")
            continue
    print(nb_billets_adulte)
    break


# Questions des billets à tarif réduit à l'utilisateur

while True :
    print("\n-> Souhaitez-vous des billets à tarif réduit et si oui combien ?")
    terminal_menu = TerminalMenu(["oui","non"])
    has_reduit = terminal_menu.show()
    if has_reduit == 0 :
        terminal_menu = TerminalMenu(["0","1","2","3","4","Choisire le nombre"])
        nb_billets_reduice = terminal_menu.show()
        if nb_billets_reduice == 5 :
            try:
                nb_billets_reduice = int(input("Nombre de billets :"))
                break
            except ValueError:
                print(chr(27) + "[2J")
                print("Merci d'utiliser des nombre")
                continue
        break
    elif has_reduit == 1 :
        nb_billets_reduice = 0
        break
        
print(nb_billets_reduice)

#Error pas de billets
if nb_billets_adulte == 0 :
        if nb_billets_reduice == 0 :
            print(chr(27) + "[2J")
            print("Sans billets vous n'irez pas loin Sagisgi ! Réesseyer..")
            conditionBillet = True
        else :
            conditionBillet = False
else :
    conditionBillet = False

# escape sequences
print(chr(27) + "[2J")  

# Questions des Gares à l'utilisateur      
while conditionGare == True:
    print("\nQuelle est votre station de départ ?")
    terminal_menu = TerminalMenu(["Meinohama","Muromi","Fujisaki","Nishijin","Tojinmachi","Ohorikoen (Ohori Park)","Akasaka","Tenjin","Nakasu-Kawabata","Gion","Hakata","Higashi-Hie","Fukuokakuko(Airport)"])
    station_start = terminal_menu.show()
    station_start_name = (stations_names[station_start])
    print("Départ : ")
    print(station_start_name)

    print("\nQuelle est votre station de d'arriver ?")
    terminal_menu = TerminalMenu(["Meinohama","Muromi","Fujisaki","Nishijin","Tojinmachi","Ohorikoen (Ohori Park)","Akasaka","Tenjin","Nakasu-Kawabata","Gion","Hakata","Higashi-Hie","Fukuokakuko(Airport)"])
    station_end = terminal_menu.show()
    station_end_name = (stations_names[station_end])
    print("Arriver : ")
    print(station_end_name)
    
    #Error same station start / end
    if station_end == station_start:
        print("Vous êtes déjà a destination.. Réesseyer en choissiant une gare d'arriver différente de celle de départ baka..")
    else :
        conditionGare = False

if stations_names[station_start:station_end] == [] :
    voie = 2



# Calcul distance
if voie == 2 :
    distance = sum(stations_distances[station_end:station_start])
else :
    distance = sum(stations_distances[station_start:station_end])

# Choix de la bonne zone tarifaire

if distance <= 3:
    tarif = 210
    Zone = 1
if distance >= 3.1:
    tarif = 270
    Zone = 2
if distance >= 7.1:
    tarif = 300
    Zone = 3
if distance >= 11.1:
    tarif = 340
    Zone = 4

# Calcul du coût total

Prix = ((nb_billets_adulte * tarif)+(nb_billets_reduice * (tarif / 2)))

# escape sequences
print(chr(27) + "[2J")

# Affichage des détails du voyage et du tarif
# Affichage de la voie du train à emprunter
# Affichage tarif celon zone tarifaire 
print("          ╭━━━┳╮╱╭┳╮╭━┳╮╱╭┳━━━┳╮╭━┳━━━╮")
print("          ┃╭━━┫┃╱┃┃┃┃╭┫┃╱┃┃╭━╮┃┃┃╭┫╭━╮┃")
print("          ┃╰━━┫┃╱┃┃╰╯╯┃┃╱┃┃┃╱┃┃╰╯╯┃┃╱┃┃")
print("          ┃╭━━┫┃╱┃┃╭╮┃┃┃╱┃┃┃╱┃┃╭╮┃┃╰━╯┃")
print("          ┃┃╱╱┃╰━╯┃┃┃╰┫╰━╯┃╰━╯┃┃┃╰┫╭━╮┃")
print("          ╰╯╱╱╰━━━┻╯╰━┻━━━┻━━━┻╯╰━┻╯╱╰╯")
print("・．━━━━━━━━━━━━ ・ RÉCAPITULATIF ・ ━━━━━━━━━━━━．・")
print("Itinéraire :")
if voie == 2 :
    print(*stations_names[station_end:station_start], sep = ", ")
else :
    print(*stations_names[station_start:station_end], sep = ", ")
print("Distance a parcourir :", round(distance),"km", "(Zone tarrifaire n°",Zone,":",tarif,") ¥")
print("Le montant a payer est de :", round(Prix),"¥","(Nombre billet adult :", nb_billets_adulte," pour ",(nb_billets_adulte * tarif),"¥ /","Nombre billet a tarif réduit :", nb_billets_reduice,"pour",nb_billets_reduice * (tarif / 2),"¥ )")
print("Votre train est sure la voix :", voie, "\nMerci de votre achat et Bon voyage !")
print("・．━━━━━━━━━━━━━━━━━━━━━ † ━━━━━━━━━━━━━━━━━━━━━．・")