"""
Cours "Intermédiaire 1" - Exercice "Journal"
"""

import argparse
from msilib.schema import Directory
import random
from re import X
from donnees import actricles
from donnees import interviews
from simple_term_menu import TerminalMenu
import os


# Import des variables nécessaires dans le module donnees

class ElementJournal():
    # Variables communes aux articles et interviews
    print(actricles)
    print(interviews)
    
    # Constructeur __init__ à écrire
    
class Article(ElementJournal):
    # Variable(s) spécifiques aux articles
    
    print(actricles.ElementJournal)

    # Constructeur __init__ à écrire

class Interview(ElementJournal):
    # Variable(s) spécifiques aux interviews    
    print(interviews.ElementJournal)
    # Constructeur __init__ à écrire

    """List all names of GitHub repositories for an org."""
     
    _

class Generateur():
    date = None
    edition = None

    # Constructeur __init__ à écrire

    def importer(self, articles, interviews):
        # Créer des instances de chaque article
        def articles(self, acticles):


        # Créer des instances de chaque interview
        
        # On rends aléatoire la liste des éléments

        # On retourne la liste des éléments

    def afficher(self):
        # Affichage des détails du journal généré
        print(f"==================================")
        print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
        print(f"==================================")
        print(f"")
        print(f"Select data directory : ")
        print(f"")
        terminal_menu = TerminalMenu(list_files(), preview_command="bat --color=always {}", preview_size=0.75)
        X = terminal_menu.show()
        if list_files(directory) == "./donnees/article.py":
        # Parcours de chaque élément, en précisant si c'est un article ou
        # une interview, et en affichant ses détails (titre, édition, contenu...)

        # Ouverture et affichage des crédits

    # Preview file finder
    def list_files(directory="./donnees/"):
        return (file for file in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, file)))
        
if __name__ == "__main__":
    
    
    
    # # On crée l'instance de ce qui nous permets d'accepter des arugments à l'aide d'argparse
    parser = argparse.ArgumentParser(description="Génère le journal du jour selon une date et une région.")
    # # On ajoute deux arguments positionnels, qui sont donc obligatoires
    parser.add_argument("date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=["national", "idf", "paca"])
    # # Argparse nous renvoie ensuite un objet contenant les valeurs des arguments
    args = parser.parse_args()

    # # Instanciation du générateur et appel de ses méthodes
    generateur = Generateur(args.date, args.edition)
    elements = generateur.importer(articles, interviews)
    generateur.afficher(elements)
