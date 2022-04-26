
# Les motifs d'URLs

Au sein d'une application Django, la variable `urlpatterns` est essentielle car elle associe un **chemin** à une **vue**. On appelle cela la [distribution des URLs](https://docs.djangoproject.com/fr/3.2/topics/http/urls/).

Ainsi, lorsque l'URL complète reçue par Django contiendra un certain **chemin**, il saura quelle **vue** utiliser pour lui transmettre la requête HTTP, et en obtenir une réponse HTTP en retour.

Par exemple, le chemin :

    testpage

Sera accessible en local à l'adresse :

    http://localhost:8000/testpage

Et, une fois l'application mise en production, à une adresse de ce genre :

    https://www.example.dev/testpage

## L'importance du slash final

Dans les URLs, chaque caractère a son importance, comme le fait d'avoir ou non un slash `/` final dans un chemin. S'il est présent, il faudra qu'il soit également présent lors de l'écriture de l'URL complète dans le navigateur ou ailleurs.

Ainsi, le chemin :

    articles/idf/

Correspondra donc à l'URL :

    http://localhost:8000/articles/idf/

Et non pas à cette URL :

    http://localhost:8000/articles/idf

## La capture de valeurs

Dans le développement web dynamique, il est courant de changer le contenu renvoyé selon ce qui est écrit dans l'URL. En tant qu'utilisateur comme en tant que développeur, cela permet de comprendre immédiatement le sens d'une URL, et ce sans avoir par exemple à utiliser de query strings du type `?name=value` à la fin de l'URL

Pour signifier à Django que des portions de notre URL seront des valeurs dynamiques, et pour avoir leur valeur accessible dans notre vue, on va les "capturer" en écrivant des chevrons `<>` au sein de notre chemin. Les chevrons contiennent le nom de notre choix qui représentera la valeur capturée, par exemple `<langue>`.

En plus de capturer des valeurs, on peut les convertir à la volée dans un type spécifique, si l'on veut s'assurer d'avoir strictement un nombre comme valeur par exemple. Pour cela, on précède le nom du type voulu : `<int:version>` au lieu de juste `<version>`. Référez-vous à la [documentation Django](https://docs.djangoproject.com/fr/3.2/topics/http/urls/#path-converters) pour une liste des types disponibles.

Dans ce chemin, on capture d'abord une valeur qui sera par défaut un `str`, puis on capturera plus loin un `int` :

    <langue>/version-<int:version>/documentation

Plusieurs URLs pourront alors correspondre à ce chemin, mais cet exemple :

    http://localhost:8000/fr/version-3/documentation

Nous donnera donc "fr" comme valeur de `<langue>`, et "3" comme valeur de `version`. Pour accéder à ces valeurs au sein d'une vue, il faudra utiliser le dictionnaire `**kwargs` de votre méthode.

## Dans le code

Pour définir un relation entre un **chemin** et une **vue**, on rajoute un élément à la liste `urlpatterns`.

Cet élément sera construit à l'aide de la fonction [path()](https://docs.djangoproject.com/fr/3.2/ref/urls/#django.urls.path) à laquelle on passe d'abord le chemin voulu, puis la fonction de la vue qui sera reliée. C'est ici que l'on peut préciser un nom qui représentera cette URL, à l'aide du mot-clé `name`.

```python
from django.urls import path

urlpatterns = [
    path("", home),
    path("<langue>/version-<int:version>/documentation", DocumentationView.as_view(), name="documentation-home"),
]
```

## Avec des expressions régulières

Pour capturer de façon plus précise les valeurs d'une URL, il est possible d'utiliser des expressions régulières (regex) à la place de la syntaxe simple proposée par Django. On utilise alors la fonction [re_path()](https://docs.djangoproject.com/fr/3.2/ref/urls/#django.urls.re_path) pour indiquer que notre chemin sera une expression régulière.

Dans l'exemple suivant, on capture la valeur "identifiant" qui sera forcément un nombre de 0 à 9, et faisant exactement 5 chiffres.

```python
from django.urls import re_path

urlpatterns = [
    re_path(r"^produits/?P<identifiant>[0-9]{5})/", ArticleView.as_view()),
]
```
