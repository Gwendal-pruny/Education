# Projet "Minimal 1"

Comme son nom l'indique, ce projet est le projet le plus petit que l'on puisse avoir lorsque l'on désire utiliser le framework Django. Pour faciliter la lecture et donc l'apprentissage, nous commençons avec tout notre code d'écrit dans un unique fichier `hello.py`.

Pour fonctionner, Django nécessite donc un minimum de paramétrage (settings), ainsi qu'au moins un motif d'URL (url pattern) qui va appeler une vue, ici sous la forme d'une simple fonction pour le moment.

## 📚 Notions

* [Settings](https://docs.djangoproject.com/fr/4.0/ref/settings/)
* [URLconf](https://docs.djangoproject.com/fr/4.0/topics/http/urls/)
* [HttpRequest](https://docs.djangoproject.com/fr/4.0/ref/request-response/#httprequest-objects) : données GET
* [HttpResponse](https://docs.djangoproject.com/fr/4.0/ref/request-response/#django.http.HttpResponse)

## ⚙️ Démarrage du projet

A défaut du classique fichier `manage.py` présent dans tous les projets Django, notre fichier unique permet d'être exécuté par Python afin d'utiliser les commandes de gestion destinées à ce dernier.

La première commande à connaître, et l'une des plus utiles, est la commande [**runserver**](https://docs.djangoproject.com/fr/4.0/ref/django-admin/#runserver) qui démarre un serveur web à des fins de développement sur votre machine :

    python hello.py runserver

Si votre système d'exploitation vous indique que le port 8000 par défaut est déjà utilisé, vous pouvez préciser le port sur lequel faire tourner le serveur comme ceci :

    python hello.py runserver 9000

## 🔗 URLs à essayer

Une fois votre serveur web local démarré, vous avez accès à plusieurs URLs qui correspondent aux motifs définis dans la variable `urlpatterns` du fichier `hello.py`.

* http://localhost:8000/
* http://localhost:8000/meteo
* http://localhost:8000/profil?nom=Test
