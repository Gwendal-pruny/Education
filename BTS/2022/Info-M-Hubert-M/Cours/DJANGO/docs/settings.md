
# La configuration Django

Pour sa [**configuration**](https://docs.djangoproject.com/fr/3.2/topics/settings/), Django utilise simplement des variables écrites au sein d'un fichier Python.

Voici les variables que vous devriez être le plus amené à modifier. Le site officiel propose bien sûr une [liste complète](https://docs.djangoproject.com/fr/3.2/ref/settings/) de ces derniers.

## DEBUG

Simple booléen permettant de dire à Django si le projet doit être utilisé en mode de développement ou non. Pour être certain de ne jamais avoir cette valeur à "vrai" en production, on ne l'écrit de préférence qu'au sein du fichier de configuration destiné à un environnement local (`debug.py`).

## SECRET_KEY

Cette variable est utilisée à de nombreux endroits par Django, par exemple pour renforcer la sécurité des informations qui doivent être salées, pour les sessions des visiteurs, etc.

Il est important de ne PAS utiliser une valeur déjà utilisée par un autre projet faisant partie de ce dépôt ou existant sur Internet, car sa valeur doit rester absolument privée. Pour chaque nouveau projet créé, vous devez donc générer une nouvelle valeur, par exemple à l'aide de [Djecrety](https://djecrety.ir/).

```python
SECRET_KEY = "zd-go$k!p0lhx2(ci@1$dox*=zo%q!!r3i!h0viuwyq(n3z(km"
```

## INSTALLED_APPS

Cette liste indique à Django les applications que vous souhaitez utiliser dans votre projet, par exemple toutes les applications contrib (authentification, sessions, interface d'administration...).

Mais il faudra également inscrire dans cette liste les applications de votre projet afin que certaines fonctionnalités fonctionnent correctement. Par exemple, si vous avez une application `mainapp` dans votre projet :

```python
INSTALLED_APPS = [
    "mainapp",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

## MIDDLEWARE

Les [**middlewares**](https://docs.djangoproject.com/fr/3.2/topics/http/middleware/) sont également des fonctionnalités proposées par Django ou par des paquets tiers que l'on peut ajouter selon nos besoins, et qui agiront sur le système des requêtes et réponses HTTP. Chaque middleware va s'ajouter l'un par-dessus l'autre, d'où parfois l'importance de les écrire dans le bon ordre.

Par exemple :

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

## ROOT_URLCONF

Représente le module Python que Django doit utiliser pour connaître les URLs du projet.

Par exemple, pour le fichier `mainapp/urls.py` :

```python
ROOT_URLCONF = "mainapp.urls"
```

## TEMPLATES

Dictionnaire contenant de nombreux paramètres utilisés par le moteur de templating de Django. C'est ici que l'on indique où chercher les templates au sein les applications, etc.

En son sein, la liste `context_processors` permet de préciser des composants Django qui pourront injecter des données très utiles dans le **contexte** dès qu'un template sera rendu en HTML.

## DATABASES

Précise les informations de connexion à une base de données, voire plusieurs lorsque nécessaire. Il est donc nécessaire de penser à dupliquer cette valeur dans les settings de production afin que notre projet Django utilise la base de données de production, etc.

La valeur `ENGINE` sert à préciser le type de base de données à laquelle vous voulez créer une connexion : MySQL, PostgreSQL, SQLite...

## STATIC_URL

Indique le dossier situé dans vos applications dans lequel se trouvent tous les fichiers statiques.
