
import sys
from datetime import datetime

from django.conf import settings
from django.urls import path
from django.http import HttpResponse

################################################################################
# Vues
################################################################################

# Pour l'instant, notre vue est une simple fonction qui doit
# renvoyer quelque chose, bien souvent une réponse HTTP comme ici
def index(request):
    heure = datetime.now().strftime("%H:%M:%S")
    html = f"""
    <h1>Django Minimal 1</h1>
    <h2>Il est {heure}.</h2>
    """
    # A peine crée avec notre contenu, l'instance de HttpResponse est renvoyée
    return HttpResponse(html)

def meteo(request):
    html = f"""
    <h1>Django Minimal 1</h1>
    <h2>Météo à Paris :</h2>
    <p>Aujourd'hui - 17°c</p>
    <p>Demain - 21°c</p>
    """
    return HttpResponse(html)

def profil(request):
    # Pour récupérer les données transmises dans l'URL (query string),
    # on va utiliser request.GET qui se comporte comme un dictionnaire
    nom = request.GET.get("nom")
    html = f"""
    <h1>Django Minimal 1</h1>
    <h2>Votre nom est : {nom}.</h2>
    """
    return HttpResponse(html)

################################################################################
# Paramètres et exécution
################################################################################

# Définition des motifs d'URLs
urlpatterns = (
    # Pour l'url "/" il sera exécuté la fonction index
    path("", index),
    # Et pour "meteo/" il sera exécuté la fonction météo
    path("meteo", meteo),
    path("profil", profil),
)

# Passage de notre configuration à Django
settings.configure(
    # Activation du mode debug
    DEBUG=True,
    # Indique à Django d'utiliser les URLS du module (fichier) en cours
    ROOT_URLCONF=__name__,
    # Clé devant rester secrète, et qui permet à Django de chiffrer ou déchiffrer des
    # informations sensibles (en base de données, dans un cookie, etc).
    # La clé ici présente a été générée aléatoirement, et il faut en faire de même pour chaque
    # nouveau projet Django : utiliser une clé aperçue sur un code public est très dangereux !
    SECRET_KEY='e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x',
)

# Les lignes qui suivent font normalement partie du fichier "manage.py"
# servant de point d'entrée à un projet Django. Cela permet donc d'avoir
# un comportement quasi équivalent au "manage.py" et d'utiliser
# les management commands.
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
