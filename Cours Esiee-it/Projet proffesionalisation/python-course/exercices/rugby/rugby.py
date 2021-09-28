
# Import des bibliothèques standard
import locale

# Import des bibliothèques tierces

# Ce code sert à indiquer à Python que l'on voudra afficher des dates
# en français lors de l'utilisation de datetime.strptime()
locale.setlocale(locale.LC_TIME, "fr_FR")

events = {}
stadiums = {}
tickets = []

# Préparation des polices

# Lecture des documents JSON

# Boucle sur chaque billet...
for ticket in tickets:
    # Préparation des textes à écrire

    # Ouverture de l'image de fond
    with Image.open("billet.png") as im:
        # Écriture des informations du match

        # Génération et écriture du QR Code

        # Sauvegarde du billet
