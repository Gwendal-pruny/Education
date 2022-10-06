from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    # À changer avec le nom de domaine de votre site web
    "www.monsiteweb.fr"
]

# Écriez là où seront compilés les fichiers statiques sur votre environnement de production (serveur...)
STATIC_ROOT = "/home/server/projetdjango/staticfiles/"
