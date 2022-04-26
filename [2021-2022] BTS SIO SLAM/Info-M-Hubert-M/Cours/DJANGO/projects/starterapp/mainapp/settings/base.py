"""
https://docs.djangoproject.com/fr/3.2/topics/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Pensez à générer une nouvelle clé à l'aide de https://djecrety.ir/
SECRET_KEY = "(io=+4*^wo@bj!i+9%m6fzptg#umjk+k6ut+m0qxyqtsytz$1p"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # On explicite l"usage de notre application pour que les templates
    # soient détectés automatiquement par Django
    # !!! Nom "mainapp" à remplacer par le nom de dossier de votre application !!!
    "mainapp"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Les URLs sont désormais déclarées dans leur propre module
# !!! Nom "mainapp" à remplacer par le nom de dossier de votre application !!!
ROOT_URLCONF = "mainapp.urls"

# !!! Nom "mainapp" à remplacer par le nom de dossier de votre application !!!
WSGI_APPLICATION = "mainapp.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/fr/3.2/ref/settings/#databases

# !!! Retirez les triple guillemets pour utiliser une base de données !!!
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # !!! A remplacer avec vos informations de connexion !!!
        'NAME': "mydatabase",
        "USER": "myuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
"""

# Password validation
# https://docs.djangoproject.com/fr/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/fr/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/fr/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/fr/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
