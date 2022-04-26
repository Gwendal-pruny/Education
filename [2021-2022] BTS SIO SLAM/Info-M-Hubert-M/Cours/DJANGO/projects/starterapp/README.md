# Projet "Starter App"

Ce projet représente le début d'un projet concret utilisant Django, tout en restant relativement minime. Plusieurs conventions sont utilisées, comme le fait d'avoir différents fichiers de paramètres selon les environnements : vous pouvez donc techniquement faire tourner ce projet "en production".

Le projet contient une application qui s'appelle `mainapp` : c'est le nom à retenir lorsque vous voudriez importer des composants de l'application quelque part en Python.

## 📚 Notions

* Séparation du code en plusieurs fichiers
* Concept des applications Django
* Paramètres différents selon l'environnement (dév & production)

## ⏩ Utilisation du projet

    python manage.py runserver

L'usage d'applications contrib entraîne le fait qu'elles puissent avoir besoin de stocker des choses dans la base de données (utilisateurs, etc). Avant cela, il faudra donc écrire les schémas nécessaires sur la base de données.

Même si votre projet ne définit pas lui-même de modèles ORM Django, vous pouvez utiliser la commande migrate pour appliquer les migrations déjà préparées par les applications contrib (incluses à Django) :

    python manage.py migrate

## 🧰 Modifications

Voici quelques guides lorsque vous voudriez travailler à partir de ce projet.

### Renommer l'application existante

Si vous souhaitez renommer le dossier `mainapp` représentant l'application principale du projet, il faudra modifier plusieurs choses à travers le projet (des imports, etc).

Pour cela, faites une recherche globale de "`!!!`" sur l'ensemble du projet pour localiser les endroits où changer le nom de l'ancienne application par son nouveau nom.

### Ajouter une vue

Pour correspondre à la façon de faire habituelle, chaque vue est contenue dans son propre fichier Python.

Après avoir créé un nouveau fichier dans le dossier `mainapp/views/`, il vous faudra ouvrir le fichier `mainapp/views/__init__.py` afin de le rendre importable par le reste de l'application.

Une fois le fichier `__init__.py` ouvert, si vous avez créé par exemple le fichier `contact.py`, écrivez-y ceci :

```python
from .contact import *
```

Ensuite, ouvrez le fichier `mainapp/urls.py` et rajoutez la classe de votre vue à la ligne qui importe toutes les vues. Par exemple, si vous aviez créé une classe `ContactView` dans le fichier `mainapp/views/contact.py`, rajoutez son nom lors de l'import :

```python
from .views import HomeView, AboutView, ContactView
```

Dans le même fichier, ajoutez une nouvelle ligne afin de relier votre nouvelle vue à une URL. N'oubliez pas que la valeur de `name` doit être absolument unique afin de pouvoir différencier chaque ligne.

```python
urlpatterns = (
    # ...
    # Les lignes existantes sont ici ...
    # ...
    path("formulaire-contact", ContactView.as_view(), name="contact"),
)
```

Pour l'exemple ci-dessus, on pourra alors accéder à cette vue en allant à l'adresse : http://localhost:8000/formulaire-contact

### Ajouter un template

Pour cela, il vous faudra d'abord insérer vos fichiers HTML dans le dossier `mainapp/templates/` afin que l'on puisse y faire référence dans une vue.

Par exemple, pour qu'une vue utilise le fichier `mainapp/templates/test.html`, il faudra y écrire cela :

```python
class TestView(TemplateView):
    template_name = "test.html"
```

### Ajouter un fichier statique

Vos fichiers statiques HTML s'accompagnent sûrement de fichiers CSS ou d'images en tout genre. Ces derniers devront être insérés dans le dossier `mainapp/static/` afin d'être utilisés dans les templates.

Pour "écrire" au sein d'un template Django le chemin vers un fichier statique, on utilise alors la [balise static](https://docs.djangoproject.com/fr/3.2/ref/templates/builtins/#static). Qu'importe comment Django (ou un serveur web, en production) fournira les fichiers statiques, l'usage de cette balise permet de toujours faire référence aux bons fichiers en écrivant la bonne URL au sein des templates.

Par exemple, pour afficher l'image `mainapp/static/osaka.jpg` dans un template Django, on importe puis utilise la balise static comme ceci :

```django
{% load static %}

<img src="{% static "osaka.jpg" %}" class="img-fluid" />
```

C'est toujours à l'endroit où l'on est censé écrire le lien vers un fichier que l'on utilise la balise static pour le faire à notre place.

### Utiliser une base de données MySQL/MariaDB

Pour faire communiquer votre projet Django avec une base de données MySQL ou MariaDB, il faudra l'indiquer au sein des paramètres du fichier `mainapp/settings/base.py` : le code nécessaire y est déjà présent, il suffit de le dé-commenter afin qu'il soit pris en compte. Recherchez les commentaires contenant `!!!` pour localiser le code.

Également, il vous faudra installer un nouveau package Python afin que Django puisse communiquer avec la base de données. Ouvrez une ligne de commande afin de l'installer comme ceci :

    pip install mysqlclient

## 🔗 URLs à essayer

* http://localhost:8000/
* http://localhost:8000/a-propos
