
# Les commandes d'administration

Bien que le monde du PHP ait habitué au fait que son site web fonctionne sans rien exécuter au préalable, ce n'est pas le cas avec la grande majorité des langages servant à faire des sites web dynamiques. Il nous faut donc généralement utiliser, au sein d'un terminal, des outils fournis par les frameworks web.

Dans le cas de Django, le principal outil s'appelle **django-admin**. Lorsque l'on a Django d'installé dans notre environnement, on peut directement l'exécuter en tapant son nom dans un terminal. Il y a cependant deux façons d'utiliser cet outil :

* Si l'on est en dehors d'un projet existant, afin de créer un nouveau projet ou pour vérifier l'installation de Django, on utilise `django-admin`.
* Si l'on est au sein d'un projet existant, on utilise `manage.py`.

Passer par `manage.py` est exactement équivalent au fait d'appeler `django-admin`, mais il permet de faire nos opérations au sein d'un projet Django existant, chose nécessaire pour la plupart des commandes.

On considère ci-dessous que le point d'entrée de votre projet Django est l'habituel `manage.py`, mais dans le cas des projets "minimal" de ce dépôt, il vous faudra remplacer cela par `hello.py`.

Lorsque vous ouvrez votre terminal pour exécuter des commandes à l'aide de `manage.py`, n'oubliez pas d'abord de naviguer vers le dossier de votre projet à l'aide de la commande `cd`.

## ⚙️ Les commandes globales

### Vérifier sa version de Django

Cette commande vous dira la version du Django qui est installée dans votre environnement actuel.

    django-admin version

### Créer un nouveau projet

Forcément très utile, cette commande va vous préparer un projet vide utilisant Django dans un nouveau dossier. Choisissez un nom court et qui ait du sens, car ce dernier sera aussi utilisé pour la création d'une application du même nom au sein du projet.

Vu que ce nom de projet et d'application devra être utilisé au sein du code source, choisissez un nom uniquement composé de lettres en minuscules.

Par exemple, pour créer le projet "portfolio" dans un nouveau dossier du même nom, puis en son sein une application "portfolio" :

    django-admin startproject portfolio

## ⚙️ Les commandes dans un projet

### Créer une nouvelle application

Pour rappel, de nombreuses fonctionnalités nécessitent d'avoir au moins 1 application au sein de son projet Django. Vu qu'un projet créé par `startproject` ne contient pas encore d'application, c'est à nous de la créer.

Ici aussi, choisissez un nom concis et clair. Si vous ne pensez pas avoir à séparer plusieurs "côtés" ou plusieurs "logiques" de votre projet en plusieurs applications, vous pouvez créer une seule application avec un nom générique comme `main`, `mainapp`, `website`, etc.

Pour créer par exemple une application nommée "website" :

    python manage.py startapp website

### Lancer son projet en mode développement

La plus importante lors du développement d'un projet Python, cette commande va lancer un serveur web de test qui vous fournira à la fois votre application Django (le côté dynamique), ainsi que les fichiers statiques de cette dernière (qui ne sont normalement pas servis au même moment).

    python manage.py runserver

Si vous avez besoin de lancer le serveur web sur un autre port que celui par défaut (8000), vous pouvez précisez le port souhaité comme ceci :

    python manage.py runserver 8080

### Shell

À des fins de débogage avancé, vous pourriez avoir l'utilité d'un REPL Python dans lequel vous pouvez directement utiliser n'importe quel module de votre projet.

    python manage.py shell

### Si l'on utilise l'ORM Django

    python manage.py makemigrations

    python manage.py showmigrations

    python manage.py migrate

    python -Xutf8 manage.py dumpdata mainapp > data.json

    python manage.py loaddata data.json

### Si l'on utilise l'app contib "auth"

    python manage.py changepassword [<username>]

    python manage.py createsuperuser

### Si l'on utilise l'app contib "static"

    python manage.py collectstatic
