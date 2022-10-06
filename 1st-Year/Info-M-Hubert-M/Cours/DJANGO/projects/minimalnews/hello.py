
import sys
import os
import json
from datetime import datetime

from django.conf import settings
from django.urls import path
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

################################################################################
# Fonctions utilitaires
################################################################################

# Tente de lire un fichier json correspondant à l'ID passé comme argument
# Renvoie un numéro représentant une erreur si la lecture est impossible
def read_article_file(id):
    path = os.path.join("data", f"{id}.json")
    article = None

    # Vérification de l'existence du fichier
    if not os.path.exists(path):
        return 404

    # Ouverture du fichier json
    try:
        with open(path, 'r', encoding="utf-8") as f:
            article = json.load(f)
    except Exception:
        return 500

    # Transforme le string sous la forme "YYYY-MM-DD" en objet datetime
    article["date"] = datetime.strptime(article["date"], "%Y-%m-%d")

    return article

# Supprime le fichier d'un article, s'il existe
def delete_article_file(id):
    path = os.path.join("data", f"{id}.json")

    # Vérification de l'existence du fichier
    if not os.path.exists(path):
        return 404

    os.remove(path)

    return True

# Écrit un nouveau fichier d'article, qui aura comme contenu
# le dictionnaire fourni à travers l'argument "data"
def write_article_file(id, data):
    path = os.path.join("data", f"{id}.json")

    with open(path, 'r', encoding="utf-8") as f:
        json.dump(data, f)

# Renvoie la liste de tous les identifiants des articles existants
# Ex : [1, 2, 3]
def get_articles_list():
    path = "data/"
    articles = []

    for entry in os.listdir(path):
        if entry.endswith(".json"):
            filename = int(os.path.splitext(entry)[0])
            articles.append(filename)

    return articles

# Utilise la fonction précédente, pour ne renvoyer que le nombre le plus élevé
def get_last_id():
    articles_ids = get_articles_list()
    articles_ids.sort()
    articles_ids.reverse()
    return articles_ids[0]

# "Middleware" qui sert à intercepter chaque réponse HTTP pour y rajouter un
# en-tête autorisant les requêtes CORS (exécutées en JavaScript par exemple)
class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response

################################################################################
# Vues
################################################################################

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        first_article = read_article_file(1)
        context["first_article"] = first_article

        return context

class ArticleView(TemplateView):
    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id = kwargs.get("id")
        article = read_article_file(id)
        context["article"] = article

        return context

class Error404View(TemplateView):
    template_name = "error_404.html"

# Vue au style API qui concerne les articles en général
class APIArticlesList(View):

    # Renvoie les identifiants de tous les articles
    def get(self, request, *args, **kwargs):
        response = {
            "articles_ids": get_articles_list()
        }
        return JsonResponse(response)

    # Crée un nouvel article
    def post(self, request, *args, **kwargs):

        # Vérification que tous les champs requis soient dans le corps
        # de la requête HTTP reçue
        mandatory_fields = ["slug", "date", "edition", "auteur","titre", "contenu"]
        for field in mandatory_fields:
            if not field in request.POST:
                response = {
                    "error": "Missing field in request body : " + field
                }
                return JsonResponse(response, status=400)

        # Devine le prochain identifiant à utiliser en récupérant le dernier existant
        next_id = get_last_id() + 1

        write_article_file(next_id, request.POST)

        response = {
            "id": next_id,
            "status": "created"
        }
        return JsonResponse(response, status=201)

# Vue au style API qui concerne un seul article en particulier (selon un ID)
class APIArticlesDetail(View):

    # Renvoie le contenu d'un article, à moins que sa lecture n'échoue
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        article = read_article_file(id)

        if article == 500:
            response = {
                "error": "An error occured when parsing the article file."
            }
            return JsonResponse(response, status=500)

        response = {
            "id": id,
            "article": article
        }
        return JsonResponse(response)

    # Supprime un article
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")

        result = delete_article_file(id)

        if result == 404:
            response = {
                "error": "The targeted article doesn't exists."
            }
            return JsonResponse(response, status=404)

        response = {
            "id": id,
            "status": "deleted"
        }
        return JsonResponse(response)

################################################################################
# Paramètres et exécution
################################################################################

urlpatterns = (
    # URLs des vues renvoyant des pages web classiques
    path("", HomeView.as_view(), name="home"),
    path("article-<int:id>-<slug:slug>", ArticleView.as_view(), name="article"),
    # URLs de nos vues "API" renvoyant exclusivement du JSON
    path("api/articles", APIArticlesList.as_view()),
    path("api/articles/<int:id>", APIArticlesDetail.as_view()),
)

handler404 = Error404View.as_view()

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="e2y8+0rx5y(e$9@b)&vn@2%v=40@3fp+1bp&w_@e*m#yr^ya7x",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                "templates",
            ],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                ],
            },
        },
    ],
    INSTALLED_APPS=[
        "django.contrib.sessions",
    ],
    MIDDLEWARE=[
        "django.contrib.sessions.middleware.SessionMiddleware",
        "__main__.CorsMiddleware"
    ],
    SESSION_ENGINE="django.contrib.sessions.backends.signed_cookies"
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
