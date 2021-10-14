"""
Cours "Introduction 2" - Exercice "Text Adventure"
"""

CHARACTERE = {
    "NAME"
    "AGE"
    "LVL"
    "PV": 70,
    "SPELL" : [
                
              ]
}

FIRST_SPELL_LIST_MAGE = [
    "Air"
    "Bois"
    "Eau"
    "Feu"
    "Métal"
    "Néant"
    "Terre"
]

FIRST_SPELL_LIST_PALADIN = [
    "Armes magique"
    "Soins légers"
    "Lumière divine"
    "Purification"
]

FIRST_SPELL_LIST_DEMON = [
    "Armes magique"
    "Peau de fer"
    "Bénédiction du sang"
    "Rage"
    "Destruction"
    "Némésis"
]

FIRST_SPELL_LIST_ASSASSIN = [
    "True Strick"
    "Secret Weapon",
    "Blade of Blood"
    "Poison Strick"
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
    message = "│[Lieux] "
    # A remplir ici
    print(message)

def proposer_actions(actions):
    message = "│[Actions] "
    # A remplir ici
    print(message)
    
def proposer_observer(oberserver):
    message ="│[Observer] "

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
    CLASS = str(input("\nQuel class souhaitez vous ? 1 -> MAGE \n 2 -> PALADIN \n 3 -> DEMON \n 4 -> ASSASSIN \n 5 -> RAMDOM"))

    
    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un
    CHARACTERE["LVL"] = 1 
    
    print("**"+(NAME)+ " à LVLUP au niveaux "+ str(CHARACTERE["LVL"]) +"**\n")
    print(FIRST_SPELL_LIST_[CLASS])
    SPELL_CHOOSE = int(input("Choissisez votre nouvelle compétance :"))
    

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
    CHARACTERE["SPELL"].append(SPELL_CHOOSE)
    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
    print(CHARACTERE)
    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************

def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["quitter"]) # À compléter
        proposer_lieux(["escalier"]) # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        # Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non

def lieu_premier_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("C'est le couloir du 1er étage.")
    print("On y trouve entre autres la classe 1-A.")

# ********************************************************************************
# EXECUTION
# ********************************************************************************

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
