/*
 * JavaScript 101
 * (1) Syntaxe
 * 🖊️ L'indentation
 * 🖊️ Écrire un commentaire
 * 🖊️ Assigner une variable
 * 🖊️ Le point-virgule
 * 🖊️ Les types de valeurs
 * 🔨 Fonctions - console.log()
 * 🖊️ Expressions booléennes
 * 🖊️ Le type primitif "undefined"
 * 🖊️ Opérateurs arithmétiques
 * 🖊️ La propriété .length
 * 🖊️ ️Lire une liste
 * 🖊️ ️Lire un objet
 * 🖊️ Concaténation
 * 🔨 Conversion vers une chaîne de caractères
 * 🔨 Conversion vers un nombre
 * 🖊️ Formatage de chaînes de caractères
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ L'indentation
/////////////////////////////////////////////////////////////////////////////////////////////
/* Bien que les avis divergent grandement sur l'usage d'espaces ou de tabulations pour écrire
 * son code JavaScript, je vous recommanderai d'utiliser 4 espaces. Les éditeurs de code
 * peuvent être paramétrés avec ce choix.
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Écrire un commentaire
/////////////////////////////////////////////////////////////////////////////////////////////
/* Vous avez pu constater qu'un commentaire tenant sur une ligne s'écrit avec // et que les
 * commentaires multi-lignes se font comme ce commentaire là à l'aide d'un slash et
 * d'une étoile. Le fait de rajouter ensuite une étoile à chaque début de ligne n'est
 * cependant que purement cosmétique.
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Assigner une variable
/////////////////////////////////////////////////////////////////////////////////////////////
/* Depuis la version ECMAScript 6, le langage propose deux nouvelles façons d'assigner une
 * variable qu'il vaut mieux utiliser au lieu du classique "var", car ils ont l'avantage de
 * toujours déclarer la variable dans le scope en cours. Pour ce qui est des noms de
 * variables, on utilise la notation "camelCase".
 */

// Le mot-clé "const" attribue une variable dont la valeur ne peut changer
const utilisateurPrenom = "Mario";

// Le mot-clé "let" attribue une variable dont la valeur peut changer,
// sa valeur est donc optionnelle
let choix;
let supplement = "Fromage";

// Pas besoin de mot-clé pour ré-attribuer une variable existante
choix = "Onigiri";

/* Si vous savez pour sûr que la valeur d'une variable ne changera jamais,
 * il vaut mieux utiliser le mot-clé "const", et sinon, le mot-clé "let"
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Le point-virgule
/////////////////////////////////////////////////////////////////////////////////////////////
/* Élément essentiel en JavaScript, c'est grâce à lui que l'on indique la fin d'une
 * déclaration. On peut donc par exemple en écrire plusieurs à la suite.
 */

let depart = "Umeda"; let destination = "Namba";


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Les types de valeurs
/////////////////////////////////////////////////////////////////////////////////////////////
/* JavaScript étant un langage à typage faible, les variables n'ont pas à préciser
 * explicitement le type des valeurs qu'elles auront. Commençons par voir quelques
 * types de valeurs dits "primitifs" :
*/

let selection = null; // null
const utilisateurNom = "Bros"; // string
const tailleMinimum = 140; // number
const isConnecte = true; // boolean
const temperature = 27.5; // number

/* Au delà de ces types primitifs, il existe le type complexe "object". La première façon
 * d'avoir un objet est de créer un collection de "propriétés" liant chacune une valeur
 * selon une clé, un peu à la façon d'un tableau associatif ou d'un dictionnaire.
 * Notez que les clés n'ont pas besoin d'être des chaînes de caractères, on peut les écrire
 * tel quel sans les entourer de guillemets
 */

// object, défini avec des accolades {}
const personnage = {
    name: "Luffy",
    age: 19
};

// D'autres choses sont également considérés comme des objets :les tableaux, les fonctions...

// Array (objet), défini avec des crochets []
const plats = ["Ramen", "Onigiri", "Udon"];

// Fonction (objet)
function getTemperature() {
    return 21;
};


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 Fonctions - console.log()
/////////////////////////////////////////////////////////////////////////////////////////////
/* Équivalent de la fonction "print" de nombreux langages, la fonction log() de la Console
 * permet de rapidement afficher n'importe quelle valeur, variable... On peut y passer un
 * un nombre infini d'arguments, qui seront alors affichés l'un après l'autre.
*/
console.log("Today temp", temperature);
console.log(getTemperature());


/////////////////////////////////////////////////////////////////////////////////////////////
// ️🖊️ Expressions booléennes
/////////////////////////////////////////////////////////////////////////////////////////////
/* Le fait de comparer des valeurs ou des variables entre elles permettent d'en avoir le
 * résultat sous forme de booléen égal à "true" ou "false". Ce genre de comparaison
 * s'appelle alors une expression booléenne.
 * On utilise des opérateurs de comparaison pour construire ces expressions :
 *     == : égalité de valeur
 *     != : inégalité de valeur
 *     === : égalité stricte de valeur
 *     !== : inégalité stricte de valeur
 *     > : supérieur à
 *     < : inférieur à
 *     >= : supérieur ou égal à
 *     <= : inférieur ou égal à
 */

const age = 21;

// Le résultat de l'expression est stockée dans une variable
const isAdulte = age > 18; // => true

// Mais on peut aussi directement utiliser le résultat
console.log(utilisateurPrenom == "Mario");

/* Les opérateurs == et != comparent des valeurs mais de façon "souple", c'est à dire
 * qu'avant la comparaison ils vont parfois convertir nos valeurs pour mieux comparer leur
 * équivalence : 0 représente par exemple la valeur "false", et 1 la valeur "true"
 */
0 == false; // => true

/* A contrario, l'usage des opérateurs stricts === et !== ne feront aucune conversion
 * au préalable et permettent de comparer réellement si deux valeurs sont
 *-strictement égales ou non
 */

0 === false; // => false

/* Lorsque l'on souhaite avoir rapidement l'inverse d'une valeur booléenne, on peut écrire
 * le caractère ! juste devant son nom : c'est l'opérateur "not"
 */
console.log(!isAdulte); // => false

/* Les opérateurs de disjonction logique permettent de composer notre expression booléenne
 * à partir de plusieurs expressions. A l'aide de l'opérateur && (and) on demande à ce que
 * le résultat de chaque expression soit "true" pour que le total soit égal à "true".
 * On peut entourer les expressions avec des parenthèses soit pour la lisibilité,
 * soit pour forcer la priorité d'évaluation comme en mathématiques.
*/

const hour = 17;
const isHappyHour = (hour >= 16) && hour <= 19; // => true

/* A contrario, on peut séparer des epxressions avec l'opérateur || (or) afin d'avoir un
 * total égal à "true" dès que l'une d'entre elles est égale à "true".
 */

const hasCouponReduction = false;
const isPrixReduit = hasCouponReduction || isHappyHour; // => true


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Le type primitif "undefined"
/* Toute variable déclarée mais dont on n'a pas attribué de valeur, se verra automatiquement
 * attribuer une valeur de type "undefined". Pour tester si une variable correspond à
 * ce type, on utilise alors le triple égal ===
 */

let testVariable;
console.log(testVariable === undefined); // => true


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Opérateurs arithmétiques
/////////////////////////////////////////////////////////////////////////////////////////////
/* Pour effectuer des opérations mathématiques, on peut utiliser ces opérateurs :
 *     + : additionne des valeurs ou des variables
 *     - : soustrait des valeurs ou des variables
 *     * : multiplie des valeurs ou des variables
 *     / : divise des valeurs ou des variables
 *     % : modulo (reste) d'une division de valeurs ou de variables
 *     ** : exposant pour élever un nombre à une puissance donnée
 */

const addition = 10 + 5;
const soustraction = 52 - 10;
const reste = 11 % 2;

/* Lorsque l'on veut simplement rajouter ou soustraire quelque chose à la valeur d'une
 * variable existante, on peut utiliser les raccourcis += et -=
 */

let colisEnvoyes = 10;

colisEnvoyes += 15;
// Équivalent à : colisEnvoyes = colisEnvoyes + 15;

colisEnvoyes -= 4;
// Équivalent à : colisEnvoyes = colisEnvoyes - 4;

/* Pour raccourcir encore plus le fait d'ajouter ou de retirer 1 à une variable, on peut
 * utiliser la notation "++" ou "--" juste après son nom
 */

let index = 5;
index++; // => 6
index--; // => 5


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ La propriété .length
/////////////////////////////////////////////////////////////////////////////////////////////
/* Utilisable sur un grand nombre de types, la propriété .length renverra la longueur de
 * quelque chose : le nombre de lettres dans une chaîne de caractères, le nombre d'éléments
 * dans une liste, etc.
 */
const villes = ["Paris", "Montreal", "Tokyo"];
console.log(villes.length); // => 3


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ ️Lire une liste
/////////////////////////////////////////////////////////////////////////////////////////////
/* Pour accéder à un élément d'une liste, il suffit de préciser entre crochets l'index
 * (numéro) de cet élément. Pour rappel, en JavaScript les listes commencent à l'index 0,
 * représentant donc le 1er élément.
 */

const boissons = ["Café", "Thé", "Soda"];
console.log(boissons[1]); // => Thé

/* Pour lire le n-ième élément en partant de la fin de la liste, il faudra "construire"
 * l'index en utilisant la longueur de la liste. L'index commençant donc à zéro, il faudra
 * donc soustraire 1 à la longueur pour correspondre au dernier élément de la liste.
 */
console.log(boissons[boissons.length - 1]); // => Soda

/* L'usage des crochets se fait de la même façon lorsque l'on souhaite accéder à une liste
 * qui est imbriquée dans une autre.
 */

const aliments = [
    ["Mangue", "Pomme"],
    ["Carotte", "Asperge"]
];
console.log(aliments[1][0]); // => Carotte


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ ️Lire un objet
/////////////////////////////////////////////////////////////////////////////////////////////
/* Lorsque l'on parle d'objet en JavaScript, cela correspond à ce que l'on appellerait un
 * dictionnaire dans d'autres langages. Il existe deux façons d'en lire les valeurs à partir
 * de ses clés : avec la notation à point, ou avec la notation à crochets.
 */
const produit = {
    name: "iPhone",
    maker: "Apple",
    "date d'achat": "15-04-2020"
};

/* La notation à point peut s'utiliser lorsque la clé que l'on souhaite lire ne possède
 * ni espaces, ni caractères spéciaux : c'est la façon la plus rapide et la plus lisible.
 * Pour permettre son usage, on conseille donc fortement de définir des clés au nom simple
 * lorsque l'on utilise des objets, facilitant alors son usage en JavaScript voire dans
 * d'autres langages (en passant du JSON par exemple)
 */
console.log(produit.name); // => iPhone

/* Quand on ne peut pas utiliser la notation à point, on peut alors lire les valeurs de
 * l'objet en utilisant des crochets comme avec une liste : on y écrira alors une clé
 * plutôt qu'un index.
 */
console.log(produit["date d'achat"]); // => 15-04-2020


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Concaténation
/////////////////////////////////////////////////////////////////////////////////////////////
/* Il est possible avec l'opérateur + de construire une chaîne de caractères à partir de
 * plusieurs valeurs. L'avantage de JavaScript est que, si l'on colle des valeurs de type
 * différents (boolean, number...), ils seront automatiquement convertis en string.
 * Les valeurs étant strictement collées, il faudra parfois prévoir des espaces, comme
 * ci-dessous autour du : par exemple.
 */
console.log("Colis envoyés : " + colisEnvoyes); // => Colis envoyés : 21


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 Conversion vers une chaîne de caractères
/////////////////////////////////////////////////////////////////////////////////////////////
/* Si besoin, il est possible de convertir explicitement une valeur en chaîne de caractères
 * grâce au constructeur String() auquel il suffit de passer la valeur à convertir.
 */

const temperatureAsString = String(40.4);
console.log(temperatureAsString); // => "40.4"


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 Conversion vers un nombre
/////////////////////////////////////////////////////////////////////////////////////////////
/* Même chose pour convertir une valeur vers un nombre, mais en utilisant Number().
 */

const httpError = Number("404");
console.log(httpError); // => 404

/* Il est bien sûr possible qu'une valeur ne puisse être convertible en nombre : dans ce
 * cas là, au lieu de générer une erreur, JavaScript vous renverra la valeur "NaN"
 * signifiant "Not a Number"
 */
const badConvert = Number("abc");
console.log(badConvert); // => NaN


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Formatage de chaînes de caractères
/////////////////////////////////////////////////////////////////////////////////////////////
/* Plutôt que de concaténer à la main des valeurs entre elles pour construire une
 * chaîne de caractères, il existe un moyen de définir une chaîne dans laquelle on peut
 * écrire directement des valeurs ou des variables Python.
 * Pour cela, on écrit notre chaîne de caractères avec le caractère "`" (backtick),
 * puis l'on pourra alors y écrire nos valeurs avec ${}
 */

const message = `La température est actuellement de ${temperature}°c.`;
console.log(message);
