# Django Course

![Logo](logo.png)

## ⚙️ Fonctionnement

Apprendre un framework web est loin d'être une tâche aisée, avec toutes les notions qu'il faut assimiler avant même de commencer un projet concret. Cependant, j'ai pu réaliser de nombreux mini-projets grâce à la polyvalence de Django, qui partent du minimum fonctionnel en un unique fichier Python, pour ensuite rajouter au fur et à mesure de nouvelles notions en avançant dans les projets.

Cependant, les projets "minimal" ne sont pas du tout utilisables dans un contexte réel ("en production"). Les projets "intro" commenceront à introduire ce qu'il faut connaître pour réaliser une mise en production fonctionnelle et surtout sûre. 

## 📚 Documentation

Pour vous faciliter l'apprentissage de Django, j'ai synthétisé certains de ses aspects dans quelques fiches. Plutôt que de constituer une réécriture de la documentation officielle, ce sont plutôt des pense-bêtes qu'il sera bon de consulter en cas d'oubli de quelque chose.

* [L'architecture de Django](docs/architecture.md)
* [Les commandes d'administration](docs/commands.md)
* [Les motifs d'URLs](docs/urls.md)
* [La configuration Django](docs/settings.md)
* [Développer son projet pas à pas](docs/process.md)
* [Mettre en production un projet Django](docs/production.md)

## ⏩ Projets

* [Minimal 1](projects/minimal1/)
  * Settings
  * URLconf
  * HttpRequest: données GET
  * HttpResponse
* [Minimal 2](projects/minimal2/)
  * URLconf : syntaxe
  * Vues : kwargs
  * HttpResponseNotFound
* [Minimal 3](projects/minimal3/)
  * Vues : classe View
  * HttpRequest : données POST
  * JsonResponse
* [Minimal 4](projects/minimal4/)
  * Fonctions shortcut : render(), redirect()
  * Templates : affichage de variables
  * Template tags : if
* [Minimal 5](projects/minimal5/)
  * TemplateView
  * Templates : variable autogénérée "request"
  * Template tags : url, for
  * Template filters : date, upper
  * Sessions
  * Handler404
* [Minimal News](projects/minimalnews/)
* [Minimal 6](projects/minimal6/)
  * Fichiers statiques
  * Templates : héritage de fichiers
* [Minimal 7](projects/minimal7/)
  * Formulaires : CharField, EmailField
  * FormView
* [Starter App](projects/starterapp/)
  * Séparation du code en plusieurs fichiers
  * Concept des applications Django
  * Paramètres différents selon l'environnement (dév & production)
* [SQL](projects/sql/)
  * Connexion à une base de données (MariaDB)
  * Requêtes SQL brutes
  * Affichage de données: requêtes SQL **SELECT** avec et sans jointures
  * Écriture de données (avec formulaire) : requêtes SQL **INSERT**
  * Mise à jour de données (avec formulaire) : requêtes SQL **UPDATE**
* [ORM](projects/orm/)
  * Interface d'administration
  * Modèles
  * TODO : DetailView
  * TODO : CreateView

En plus des projets, vous pouvez retrouver les cours et entraînements réalisés en classe dans le dossier [livecoding](livecoding/).

## 🏗️ Préparer son environnement

1. Tout d'abord, vous pouvez créer un environnement virtuel puis l'activer avant de commencer à travailler avec l'un des projets, mais cela reste optionnel
2. Django s'installe grâce à PIP avec la commande `pip install Django` (ou `pip3`)
3. Le fichier README vous précisera ensuite la commande à taper dans son terminal pour lancer le projet ou exécuter d'autres opérations

## 🧰 Applications utiles

Pour facilement créer des requêtes HTTP afin de tester une application web ou une API :

* [Advanced REST Client](https://install.advancedrestclient.com/install) (Windows, Linux, macOS)

Pour manipuler une base de donnée MySQL ou MariaDB, je vous recommande les applications suivantes :

* [TablePlus](https://tableplus.com/) (Windows, Linux, macOS) avec version d'essai illimitée
* [HeidiSQL](https://www.heidisql.com/) (Windows) fourni avec MariaDB

Pour manipuler une base de données PostgreSQL, je vous recommande cette application web :

* [pgAdmin](https://www.pgadmin.org/) (Windows, Linux, macOS)
