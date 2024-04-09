import csv

class Film:
    def __init__(self, titre, realisateur, annee, genre, cout, recette):
        self.titre = titre
        self.realisateur = realisateur
        self.annee = annee
        self.genre = genre
        self.cout = cout
        self.recette = recette
        self.liste_acteurs = []

    def __str__(self):
        acteurs = ', '.join([acteur.nom for acteur in self.liste_acteurs])
        return f"Titre: {self.titre}, Realisateur: {self.realisateur}, Annee: {self.annee}, Genre: {self.genre}, " \
               f"Acteurs: {acteurs}, Cout: {self.cout}, Recette: {self.recette}"

    @staticmethod
    def create_film():
        print("Création d'un film...\n")
        titre = input("Entrez le nom du film: ")
        realisateur = input("Entrez le nom du réalisateur: ")
        annee = int(input("Entrez l'année de sortie: "))
        genre = input("Entrez le genre: ")
        cout = int(input("Entrez le cout: "))
        recette = int(input("Entrez la recette: "))
        film = Film(titre, realisateur, annee, genre, cout, recette)
        acteurs_input = input("Entrez le nom des acteurs (séparés par des virgules): ")
        acteurs_names = [nom.strip() for nom in acteurs_input.split(",")]
        film.liste_acteurs = [Acteur(nom) for nom in acteurs_names]
        print("------------------")
        print("Le film a été créé avec succès :")
        print(film)  # Print the film details
        print("------------------")
        return film

    def print_acteurs(self):
        print(f"Acteurs du film: {[acteur.nom for acteur in self.liste_acteurs]}")

    def nb_acteurs(self):
        print(f"Nombre d'acteurs dans le film: {len(self.liste_acteurs)}")

    def calcul_benefice(self):
        benefice = self.recette - self.cout
        print(f"Calcul bénéfice: {benefice}")

    def is_before(self, annee):
        print("A été crée avent 2023 : "+ str(self.annee < annee))

    def nb_personnages(self):
        total = sum(len(acteur.personnages) for acteur in self.liste_acteurs)
        print("Nombre de personnage :"+str(total))

    def tri(self):
        self.liste_acteurs.sort(key=lambda acteur: acteur.nom)

liste_acteurs = []
liste_personnages = []
class Acteur:
    def __init__(self, nom, prenom=None, films_joues=None, personnages=None):
        self.nom = nom
        self.prenom = prenom
        self.films_joues = films_joues if films_joues is not None else []
        self.personnages = personnages if personnages is not None else []

    def __str__(self):
        films = ', '.join(self.films_joues)
        personnages = ', '.join(self.personnages)
        return f"Nom: {self.nom}, Prenom: {self.prenom}, Films joués: {films}, Personnages: {personnages}"

    @staticmethod
    def create_acteur():
        print("Création d'un acteur...\n")
        nom = input("Entrez le nom de l'acteur: ")
        prenom = input("Entrez le prénom de l'acteur: ")
        films_input = input("Entrez les films dans lesquels l'acteur a joué (séparés par des virgules): ")
        films_joues = [film.strip() for film in films_input.split(",")]
        personnages_input = input("Entrez les personnages que l'acteur a joués (séparés par des virgules): ")
        personnages = [personnage.strip() for personnage in personnages_input.split(",")]
        acteur = Acteur(nom, prenom, films_joues, personnages)
        liste_acteurs.append(acteur)  # Add the actor to the list
        print(f"L'acteur a été créé avec succès :\n{str(acteur)}")
        return acteur
    
class Personnage:
    def __init__(self, nom, prenom, pseudonyme):
        self.nom = nom
        self.prenom = prenom
        self.pseudonyme = pseudonyme

    def __str__(self):
        return f"Nom: {self.nom}, Prenom: {self.prenom}, Pseudonyme: {self.pseudonyme}"

    @staticmethod
    def create_personnage():
        print("Création d'un personnage...\n")
        print("Choisissez le côté obscur de la force : Sith")
        pseudonyme = input("Entrez le pseudonyme: ")
        nom = input("Entrez le nom: ")
        prenom = input("Entrez le prénom: ")
        personnage = Personnage(nom, prenom, pseudonyme)
        liste_personnages.append(personnage)  # Add the character to the list
        return personnage


def make_backup(films):
    with open('backup.txt', 'w') as file:
        writer = csv.writer(file, delimiter='-')
        for key, film in films.items():
            line = f"{key} - {film.titre} - {film.recette - film.cout}"
            writer.writerow([line])
    with open('backup_acteurs.txt', 'w') as f:
        for acteur in liste_acteurs:
            f.write(str(acteur) + '\n')
    with open('backup_personnages.txt', 'w') as f:
        for personnage in liste_personnages:
            f.write(str(personnage) + '\n')


def main():
    collection = []
    films = {}
    while True:
        try:
            print("\n=========== Menu =============")
            print("1. Créer un film")
            print("2. Créer un acteur")
            print("3. Créer un personnage")
            print("4. Afficher la collection de films")
            print("5. Trier les acteurs par ordre alphabétique")
            print("6. Créer une sauvegarde")
            print("7. Lister les acteurs")  # New option to list actors
            print("8. Lister les personnages")  # New option to list characters
            print("9. Quitter")  # Updated quit option
            option = int(input("Choisissez une option: "))
            if option == 1:
                film = Film.create_film()
                collection.append(film)
                films[len(films) + 1] = film
            elif option == 2:
                Acteur.create_acteur()
            elif option == 3:
                Personnage.create_personnage()
            elif option == 4:
                print("\n=========== Collection de films =============")
                for film in collection:
                    print(film)
                    print("=========== Acteurs =============")
                    film.print_acteurs()
                    film.nb_acteurs()
                    film.calcul_benefice()
                    film.is_before(2023)
                    print("=========== Personnages =============")
                    film.nb_personnages()
            elif option == 5:
                for film in collection:
                    film.tri()
                print("Les acteurs ont été triés par ordre alphabétique.")
            elif option == 6:
                make_backup(films)
                print("Une sauvegarde a été créée.")
            elif option == 7:  # New elif block to handle listing actors
                for acteur in liste_acteurs:
                    print(acteur)
            elif option == 8:  # New elif block to handle listing characters
                for personnage in liste_personnages:
                    print(personnage)
            elif option == 9:
                print("Au revoir!")
                break
        except ValueError:
            print("Erreur de frappe. Veuillez entrer un nombre.")

if __name__ == "__main__":
    main()