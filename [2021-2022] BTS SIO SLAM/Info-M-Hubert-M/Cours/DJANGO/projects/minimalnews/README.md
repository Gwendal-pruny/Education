# Projet "Minimal News"

Ce projet est basé sur le projet "Minimal 5". Il n'apprends aucune nouvelle notion, mais il utilise celles vues à partir du projet "Minimal 1" jusqu'à "Minimal 5".

Il représente un mini-site permettant d'afficher de courts articles d'actualités, stockés dans de simples fichiers JSON afin de ne pas s'encombrer d'une base de données. En plus de fournir plusieurs pages HTML, il fournit surtout des URLs ressemblant à celle d'une API.

Le code est moins commenté que d'habitude pour vous laisser comprendre le fonctionnement du projet, et pour faciliter un peu la lecture.

En plus du projet Django stocké intégralement dans le fichier `hello.py`, il vous est mis à disposition un script Python dans le fichier `apicalls.py`. Ce dernier vous permet d'appeler les URLs (appelées "endpoints") grâce à l'usage de la bibliothèque [requests](https://docs.python-requests.org/en/master/).

## ⏩ Démarrage du projet

    python hello.py runserver

Pour utiliser le fichier `apicalls.py` et ses fonctions, vous pouvez écrire les commandes suivantes :

    python apicalls.py get-articles

    python apicalls.py post-articles

    python apicalls.py delete-article

## 🔗 URLs à essayer

* GET http://localhost:8000/
* GET http://localhost:8000/article-1-vague-froid-pays
* GET http://localhost:8000/api/articles
* POST http://localhost:8000/api/articles
* GET http://localhost:8000/api/articles/1
* DELETE http://localhost:8000/api/articles/1
