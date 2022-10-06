
# Développer son projet pas à pas

## 1) Créer le projet

Pour cela, vous pouvez soit utiliser l'outil [**django-admin**](commands.md) afin de préparer les dossiers et fichiers de base requis, soit copier le projet [**starterapp**](../projects/starterapp/README.md) présent dans ce dépôt.

## 2) Éditer la configurations

Pour rappel, la configuration (settings) est l'élément principal qui va permettre à Django de faire tourner votre site web, et qui reliera tous les composants entre eux.

C'est donc la première chose qu'il vous faudra modifier afin que les paramètres correspondent à ce que vous souhaitez faire. Bien que `django-admin` ne crée qu'un seul fichier par défaut, on préférera découper la configuration en 3 fichiers :

* Un fichier avec toute la configuration de base (par exemple `settings/base.py`)
* Un fichier avec uniquement les paramètres correspondant à l'environnement de développement (par exemple `settings/debug.py`)
* Un fichier avec uniquement les paramètres correspondant à l'environnement de production (par exemple `settings/prod.py`)

Si vous passez d'un fichier à plusieurs fichiers, il vous faudra modifier en conséquence deux fichiers : `manage.py` pour l'environnement de développement et `wsgi.py`/`asgi.py` pour l'environnement de production.

Par exemple, pour une application s'appelant `mainapp` et ayant un fichier `settings/debug.py`, il faudra modifier une certaine ligne du fichier `manage.py` comme ceci :

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings.debug')

Pour les fichiers `wsgi.py` et `asgi.py`, il faudra modifier une ligne similaire, pour pointer vers le fichier `settings/prod.py` :

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings.prod')

Référez vous à la [documentation sur la configuration](settings.md) pour savoir comment remplir chaque variable.

**Attention :** Changez dès maintenant la valeur de variable `SECRET_KEY`. Si vous le faites plus tard parce que vous aviez oublié de le faire, il est possible que cela casse certaines choses qui se basent dessus (mots de passe des utilisateurs Django, etc).

# 3) Préparer les vues

Pour renvoyer quelque chose à un visiteur ou à une application contactant une API, il faudra systématiquement commencer par créer des **vues**. Ces dernières pourront renvoyer des **templates** ou bien directement des **données brutes**.

On peut simplifier grossièrement en disant qu'une page de votre site web corresponde à une vue.

# 4) Connecter les vues à des URLs

Afin d'être utilisées, les vues doivent être reliées à des URLs : c'est le rôle du fichier `urls.py`. Pour cela, commencez par importer la vue qui vous intéresse, puis créez une nouvelle ligne au sein du tuple `urlpatterns`. Consultez la [documentation des URLs](urls.md) pour en savoir plus sur ce sujet.

# 5) Préparer les templates utilisées par vos vues

Chaque page web aura logiquement son propre template HTML, mais pour éviter de dupliquer notre code, on fait généralement en sorte que chacune de ces templates **hérite** d'un template commun (par exemple `base.html`).

# 6) Préparer les modèles

TODO
