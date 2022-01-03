"""
Cours "Introduction 2" - Exercice "Text Adventure"
"""
import yaml

CHARACTERE = {
    "NAME"
    "AGE"
    "LVL"
    "PV": 70,
    "SPELL" : [
                
              ]
}

SPELL_LIST_MAGE = [
    "Air",
    "Bois",
    "Eau",
    "Feu",
    "Métal",
    "Néant",
    "Terre"
]

SPELL_LIST_PALADIN = [
    "Armes-magique",
    "Soins-légers",
    "Lumière-divine",
    "Purification"
]

SPELL_LIST_DEMON = [
    "Armes-magique",
    "Peau-de-fer",
    "Bénédiction-du-sang",
    "Rage",
    "Destruction",
    "Némésis"
]

SPELL_LIST_ASSASSIN = [
    "True-Strick",
    "Secret-Weapon",
    "Blade-of-Blood",
    "Poison-Strick"
]

KEYS_INVENTORY = [
    
]

FOOD = [
        "Ramen",
        "Onigiri",
        "Udon",
        "Curry"
        ] # À transformer en liste

FOOD_STOCK = {"Ramen", "Onigiri", "Udon", "Curry"} # À remplir avec les plats

KEYS = ["smartphone"]
INVENTORY = {"Ramen"}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************

def proposer_lieux(mots_cles):
    message = "│"+mots_cles
    # A remplir ici
    print(message)

def proposer_actions(actions):
    message = "│"+actions
    # A remplir ici
    print(message)
    
def proposer_observer(oberserver):
    message = "│"+oberserver
    
    print(message)


def lvlup(CLASS, LVL):

    #for the first lvlup
    if LVL == 1:
        if CLASS == "MAGE":
            print("│ Choissisez votre premier sort MAGE:")
            print(*SPELL_LIST_MAGE)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_MAGE:
                SPELL_LIST_MAGE.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")

        
        if CLASS == "PALADIN":
            print("│ Choissisez votre premier sort PALADIN:")
            print(*SPELL_LIST_PALADIN)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_PALADIN:
                SPELL_LIST_PALADIN.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")

        
        if CLASS == "DEMON":
            print("│ Choissisez votre premier sort DEMON:")
            print(*SPELL_LIST_DEMON)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_DEMON:
                SPELL_LIST_DEMON.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")

        if CLASS == "ASSASSIN":
            print("│ Choissisez votre premier sort ASSASSIN:")
            print(*SPELL_LIST_ASSASSIN)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_ASSASSIN:
                SPELL_LIST_ASSASSIN.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")


    #for higher than lvl 1
    else :
        if CLASS == "MAGE":
            print("│ Choissisez votre premier sort MAGE")
            print(*SPELL_LIST_MAGE)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_MAGE:
                SPELL_LIST_MAGE.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")
        if CLASS == "PALADIN":
            print("│ Choissisez votre premier sort PALADIN")
            print(*SPELL_LIST_PALADIN)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_PALADIN:
                SPELL_LIST_PALADIN.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")
        if CLASS == "DEMON":
            print("│ Choissisez votre premier sort DEMON ")
            print(*SPELL_LIST_DEMON)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_DEMON:
                SPELL_LIST_DEMON.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")

        if CLASS == "ASSASSIN":
            print("│ Choissisez votre premier sort ASSASSIN ")
            print(*SPELL_LIST_ASSASSIN)
            SPELL_CHOOSE = str(input("CHOIX : "))

            if SPELL_CHOOSE in SPELL_LIST_ASSASSIN:
                SPELL_LIST_ASSASSIN.remove(SPELL_CHOOSE)
                CHARACTERE["SPELL"].append(SPELL_CHOOSE)
            else :
                print("Invalide input - RETRY")

def printCharacter():
    print("┌──────────── CHARACTERE ───────────────")
    print(yaml.dump(CHARACTERE))
    print("└──────────── CHARACTERE ───────────────")





# ********************************************************************************
# INTRODUCTION
# ********************************************************************************

def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")
    AGE = int(input("\nQuel âge as-tu ?\n\n\n\n"))
    NAME = str(input("\nQuel nom as-tu ?\n\n\n\n"))
    CLASS = str(input("\nQuel class souhaitez vous ?\n 1 -> MAGE \n 2 -> PALADIN \n 3 -> DEMON \n 4 -> ASSASSIN \n 5 -> RAMDOM\n"))


    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un
    CHARACTERE["LVL"] = 1 
    print("** "+(NAME)+ " à LVLUP au niveaux "+ str(CHARACTERE["LVL"]) +" **\n")
    lvlup(CLASS, LVL = CHARACTERE["LVL"])    

    
    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
    printCharacter()
        
    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************

# ENTRE DANS LE HALL

def lieu_hall():
    LIEUX = "lieu_hall"
    print(chr(27) + "[2J")
    printCharacter()
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

# REDIRECTION ACTIVITE

    while True:
        print("┌────────────────────────────────────────")
        proposer_observer("│1.Esseyer de rentré dans les différentes pièces")
        proposer_actions("│2.Quitter le hall") # À compléter
        proposer_lieux("│3.Prendre les escalier vers le niveaux supérieur") # À compléter
        reponse = input("││Choisir le nombre correspondant a votre choix├─> ")
        print("└────────────────────────────────────────")
        if reponse == 1 :
            SpaceOptionsObserver(lieux_hall)
        elif reponse == 2 :
            SpaceOptionsAction(lieu_hall)
        elif reponse == 3 :
            SpaceOptionsLieux(lieu_hall)

# ENTRE DANS LE PREMIER ETAGE

def lieu_premier_etage():
    print(chr(27) + "[2J")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("C'est le couloir du 1er étage.")
    print("On y trouve entre autres la classe 1-A.")


# ********************************************************************************
# GAME ADVENTUREEEEEEEEEEE
# ********************************************************************************

# *******************************       HALL        ******************************


def SpaceOptionsObserver(LIEUX):
    if SpaceOptionsObserver.lieux == "lieu_hall":
        print("│1.[Acceuil] \n")
        print("│2.[Bureau du proviseur] \n")
        print("│3.[Infirmerie] \n")
        print("│4.[BDE] \n")
        print("│5.[Super Secret Door] \n")
        print("|6.[Prendre les escalier vers le niveaux supérieur]")
        print("|7.[Quitter le hall]") # À compléter
        reponse = input("[Choisir le nombre correspondant a votre choix]├─> ")
        if reponse == 1 :
            if "FIRSTKEY" in KEYS_INVENTORY :
                print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("Bienvenue à l'acceuil !")
                print("Avez vous besoin de renseignement ?")
                print("│1.[Oui] \n")
                print("│2.[Non] \n")
                reponse = input("├─> ")
                if reponse == 1 :
                    print("Ta classe est situer a l'étage tu devrais allez voir t'es cammarade.")
                elif reponse == 2 :
                    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("Tu est revenue dans le hall")
                    SpaceOptionsObserver(lieu_hall)

            else :
                print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("Bizzarement personne a l'acceuil...")
                print("Partir ?")
                print("│1.[Oui] \n")
                print("│2.[Non] \n")
                if reponse == 2 :                    
                    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("Tu t'ennui personne ne vient tu repart dans le hall")
                    SpaceOptionsObserver(lieu_hall)
                elif reponse == 1 :
                    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("Tu est revenue dans le hall")
                    SpaceOptionsObserver(lieu_hall)


# *******************************   PREMIER ETAGE   ******************************

def SpaceOptionsObserver(LIEUX):
    if SpaceOptionsObserver.lieux == "premier_etage":
        print("│1.[Acceuil] \n")
        print("│2.[Bureau du proviseur] \n")
        print("│3.[Infirmerie] \n")
        print("│4.[BDE] \n")
        print("│5.[Super Secret Door] \n")
        print("|6.[Prendre les escalier vers le niveaux supérieur]")
        print("|7.[Quitter le hall]") # À compléter
        reponse = input("[Choisir le nombre correspondant a votre choix]├─> ")





# ********************************************************************************
# EXECUTION
# ********************************************************************************

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
