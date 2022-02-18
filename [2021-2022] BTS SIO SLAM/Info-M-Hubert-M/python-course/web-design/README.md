# Web Design

![Logo](logo.png)

## ⚙️ Fonctionnement

Ce cours regroupe les bases du web-design dit "front-end", c'est à dire le côté du développement web qui se passe dans le navigateur web.

En plus de fichiers expliquant les bases du HTML et du CSS, d'autres expliquent l'usage basique du framework CSS [Bootstrap](https://getbootstrap.com/).

Le cours sur le langage JavaScript consiste en des fichiers qui peuvent s'exécuter tel un script sur Node.js, ou directement dans son IDE grâce à l'extension [Quokka.js](https://marketplace.visualstudio.com/items?itemName=WallabyJs.quokka-vscode) par exemple.

Le cours sur l'usage du JavaScript dans un contexte de navigateur est composé de fichiers HTML et JS afin d'apprendre dans un contexte réel. Bien sûr, il est vivement recommandé d'ouvrir les DevTools (et sa console) de son navigateur lorsque vous consulterez les fichiers HTML.

## ⏩ Chapitres

### HTML & CSS 101

1. [Éléments](html-css-101/1-elements.html)
2. [Formulaires](html-css-101/2-form.html)
3. [Tableaux](html-css-101/3-table.html)
4. [Flexbox](html-css-101/4-flexbox.html)
5. [Éléments avancés](html-css-101/5-advanced.html)

### Bootstrap 101

1. [Mise en page](boostrap-101/1-layout.html)
2. [Composants](boostrap-101/2-components.html)
3. [Formulaires](boostrap-101/3-form.html)

### JavaScript 101

* [1. Syntaxe](javascript-101/1-syntax.js)
  * 🖊️ L'indentation
  * 🖊️ Écrire un commentaire
  * 🖊️ Assigner une variable
  * 🖊️ Le point-virgule
  * 🖊️ Les types de valeurs
  * 🔨 Fonctions - `console.log()`
  * 🖊️ Expressions booléennes
  * 🖊️ Le type primitif "undefined"
  * 🖊️ Opérateurs arithmétiques
  * 🔨 La propriété `.length`
  * 🖊️ ️Lire une liste
  * 🖊️ ️Lire un objet
  * 🖊️ Concaténation
  * 🔨 Conversion vers une chaîne de caractères
  * 🔨 Conversion vers un nombre
  * 🖊️ Formatage de chaînes de caractères
* [2. Déclarations](javascript-101/2-statements.js)
  * 🖊️ ️Les structures conditionnelles - `if` / `else if` / `else`
  * 🖊️ ️L'opérateur conditionnel "?"
  * 🖊️ La boucle `for`
  * 🖊️ La boucle `for...of`
  * 🖊️ La boucle `for...in`
  * 🖊️ La boucle `while`
  * 🖊️ L'instruction `switch`
* [3. Objets](javascript-101/3-objects.js)
  * 🔨 Créer un objet
  * 🔨 Manipuler une chaîne de caractères
  * 🔨 ️Manipuler une liste
  * 🔨 ️Manipuler un objet
* [4. Fonctions](javascript-101/4-functions.js)
  * ️🖊️ Les fonctions
  * ⚙️ Le passage des variables
  * ⚙️ La portée des variables
  * ️🖊️ Les fonctions anonymes
  * 🖊️ Le déballage de valeurs
* [5. Orienté Objet](javascript-101/5-oop.js)
  * 🖊️ Les classes, attributs et méthodes
  * 🖊️ L'héritage
  * 🖊️ La capture des exceptions - `try` / `catch`
  * 🖊️ La levée d'exceptions - `throw`

### JavaScript front-end

1. [DOM](javascript-front/1-dom.html)
2. [Events](javascript-front/2-events.html)
3. [Fetch](javascript-front/3-fetch.html)

## 🔍 Approfondir

Il est important de toujours consulter des documentations de qualité et toujours à jour. Faites donc attention aux sites tels que W3Schools qui, bien qu'ayant le mérite d'être concis, ne sont pas souvent actualisés.

* La documentation [MDN Web Docs](https://developer.mozilla.org/fr/docs/Web#web_technology_references)
* Les tutoriels de l'agence web [AlsaCréations](https://www.alsacreations.com/tutoriels/)
* Une antisèche des [courbes d'accélération](https://easings.net/fr) (easings) utilisées lors d'animations CSS

De plus, de nombreux outils existent pour vous faciliter le développement web.

### CSS

* Les guides de [CSS Tricks](https://css-tricks.com/guides/)
* Un [générateur de dégradés](https://cssgradient.io/) CSS
* Un [guide à Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
* Une [aide interactive à Flexbox](https://devinduct.com/workshop/flexbox)

### JavaScript

* La documentation JavaScript de [MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript)
* Les tutoriels de [Javascript.info](https://javascript.info/)
* Les articles de [JavaScriptTutorial](https://www.javascripttutorial.net/)
* Ma [série d'articles de blog](https://blog.michaelhubert.me/javascript-bizarre-adventure-part-1-moteurs/) sur JavaScript

### SQL

* Les articles de [SQL.sh](https://sql.sh/)

### SEO et assimilés

* Un [générateur de favicon](https://realfavicongenerator.net/) sous de nombreux formats

## 🏗️ Préparer son environnement

Pour faciliter la lecture des fichiers HTML/CSS ainsi que leur modification, on peut utiliser VS Code avec l'extension [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).

Une fois l'extension installée dans VS Code, lorsque l'on ouvre un fichier HTML, il faut ouvrir le panneau de commandes (`Ctrl+Shift+P` ou `⇧⌘P`) et lancer la commande "Open with Live Server". Un lien s'ouvrira alors automatiquement dans votre navigateur, et la page sera rechargée à chaque modification d'un fichier du projet.
