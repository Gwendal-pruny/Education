# Projet "SQL"

Requêtes SQL brutes (raw), c'est à dire "à la main" sans utiliser l'ORM inclus avec Django. Nous apprendrons à utiliser ce dernier plus tard.

## 📚 Notions

* Connexion à une base de données (MariaDB)
* Requêtes SQL brutes : [exécution directe de code SQL](https://docs.djangoproject.com/fr/3.2/topics/db/sql/#executing-custom-sql-directly)
* Affichage de données: requêtes SQL **SELECT** avec et sans jointures
* Écriture de données (avec formulaire) : requêtes SQL **INSERT**
* Mise à jour de données (avec formulaire) : requêtes SQL **UPDATE**

## ⚠️ Prérequis

* Avoir un serveur MariaDB en cours d'exécution
* Avoir une base de donnée initialisée avec le schéma et les données du fichier "[database.sql](database.sql)"
* Configurer le fichier `mainapp/settings/base.py` de ce projet avec les informations de connexion à votre base de données MariaDB installée sur votre ordinateur (port, utilisateur, mot de passe)
* Exécuter `pip install mysqlclient` (ou `pip3`) dans une invite de commandes, afin d'installer le paquet prérequis à l'usage d'une base de données MySQL/MariaDB avec Django

## ⏩ Démarrage du projet

Avant de démarrer le projet Django, n'oubliez pas de démarrer votre base de données MariaDB (à travers les Services sur Windows, ou en écrivant `mysql.server start` sur macOS)

    python manage.py runserver

_Il vous faudra peut-être remplacer `python` par `python3` selon votre environnement (macOS...)_

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/stadiums
* http://localhost:8000/newsletter
* http://localhost:8000/update
