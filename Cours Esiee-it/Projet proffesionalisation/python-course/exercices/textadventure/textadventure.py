"""
Cours "Introduction 2" - Exercice "Text Adventure"
"""

personnage = {
    "PV": 70
}

pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite"
]

plats = "Ramen,Onigiri,Udon,Curry" # À transformer en liste

plats_stock = {} # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}

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
    print("\nQuel âge as-tu ?")

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"
    
    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
    
    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"

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
