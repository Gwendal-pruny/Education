/*
 * JavaScript 101
 * (2) Déclarations
 * 🖊️ ️Les structures conditionnelles - if / else if / else
 * 🖊️ ️L'opérateur conditionnel "?"
 * 🖊️ La boucle for
 * 🖊️ La boucle for...of
 * 🖊️ La boucle for...in
 * 🖊️ La boucle while
 * 🖊️ L'instruction switch
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ ️Les structures conditionnelles - if / else if / else
/////////////////////////////////////////////////////////////////////////////////////////////
/* Les expression booléennes, vues dans le chapitre précédent, s'utilisent généralement au
 * sein de structures conditionnelles, qui vont exécuter un bout de code ou un autre selon
 * si l'expression équivaut à vrai ou faux. La base de tout code informatique en somme !
 * La structure "if" étant un bloc, on écrit l'expression booléenne entre parenthèses,
 * puis le code à exécuter entre accolades.
 */

if (100 < 404) {
    console.log("100 est bien inférieur à 404.");
}

/* Si l'on veut exécuter un autre morceau de code dans le cas où l'expression booléenne
 * soit fausse, on peut ajouter à la fin du bloc existant un "else" avec un nouveau bloc.
 */

let weather = "sunny";

if (weather == "cloudy") {
    console.log("Il fait nuageux");
} else {
    console.log("Il n'y a pas spécialement de nuages");
}

/* Pour représenter des conditions plus complexes, on peut vérifier si d'autres expressions
 * sont vraies ou fausses lorsque le premier "if" est faux. On utilise donc des "else if",
 * et lorsqu'une expression est vraie, son code sera exécuté, sans exécuter le reste.
 */

weather = "rainy";

if (weather == "cloudy") {
    console.log("Il fait nuageux");
} else if (weather == "rainy") {
    console.log("Il pleut");
} else {
    console.log("Aucune idée de la météo");
}


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ ️L'opérateur conditionnel "?"
/////////////////////////////////////////////////////////////////////////////////////////////
/* Lorsque l'on souhaite tout simplement attribuer une valeur différente à une variable en
 * fonction d'une expression booléenne, il existe une façon raccourcie de faire cela.
 * Voyons d'abord comment l'on ferait avec un simple "if" comme vu précédemment.
 */
const age = 22;

let message = "";
if (age > 18) {
    message = "Autorisé";
} else {
    message = "Interdit";
}

/* Ce genre d'attribution de valeur très simple, selon si une expression booléenne est vraie
 * ou fausse, peut s'écrire de façon raccourcie avec l'opérateur conditionnel "?".
 * A droite du nom de notre variable, où s'écrit normalement la valeur souhaitée,
 * on écrit alors comme ceci :
 * (expression booléenne) ? (valeur si vrai) : (valeur si faux)
 */

const alerte = age > 18 ? "Autorisé" : "Interdit"; // => "Autorisé"


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ La boucle for
/////////////////////////////////////////////////////////////////////////////////////////////
/* Destinée à exécuter le même code plusieurs fois de suite, la boucle "for" réalise cela à
 * l'aide d'un nombre qui augmente ou réduit de valeur, afin de suivre le nombre de fois
 * que le code a été exécuté et afin de savoir quand il faudra s'arrêter.
 * Chaque "exécution de code" par la boucle s'appelle alors une "itération".
 * La variable est d'abord déclarée (généralement "i" par convention) avec sa valeur
 * de départ, puis on décide de l'expression booléenne qui exécutera la boucle "for" tant
 * que sa valeur est vraie, et enfin on décide de comment la variable sera modifiée
 * après chaque itération.
 * Attention, cette variable étant déclarée dans le bloc "for", elle ne sera pas disponible
 * en dehors de ce dernier.
 */

// En partant à zéro ; tant que i est inférieur à 4 ; en ajoutant 1 à i après chaque itération
for (let i = 0; i <= 4; i++) {
    console.log(`Itération n°${i}`);
}

// En partant de 3 ; tant que i est supérieur à 0 ; en soustrayant 1 à i après chaque itération
for (let i = 3; i > 0; i--) {
    console.log(`Itération n°${i}`);
}


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ La boucle for...of
/////////////////////////////////////////////////////////////////////////////////////////////
/* La façon la plus simple d'itérer sur les valeurs de quelque chose est d'utiliser le
 * bloc "for" en utilisant le mot-clé "of". On décide alors du nom de la variable qui
 * aura pour valeur l'élément lu lors d'une itération sur une liste (ou quelque chose
 * qui s'y ressemble).
 */

const hotDrinks = ["Espresso", "Cappuccino", "Mochaccino"];

// Pour chaque "coffee" dans "hotDrinks"
for (const coffee of hotDrinks) {
    console.log(coffee);
}

/* On peut aussi utiliser ce "for" sur les choses qui sont semblables à une liste,
 * comme une chaîne de caractères. L'élément parcouru sera alors une lettre.
 */
// Pour chaque "lettre" de la chaîne "Shinkansen"
for (const letter of "Shinkansen") {
    console.log(letter);
}

/* Si l'on souhaite itérer sur un objet tout en ayant à la fois la clé et la valeur
 * parcourue à chaque itération, il faudra faire appel à la fonction Object.entries().
 * Ce dernier crée à la volée une version itérable de notre objet, renvoyant alors
 * une liste à chaque itération contenant d'abord la clé puis la valeur parcourue.
 */

const subwayLine = {
    name: "Asakusa",
    company: "Tokyo Metro",
    opening: 1927
};

// Pour chaque couple de clé et valeur dans l'objet "subwayLine"
for (const [key, value] of Object.entries(subwayLine)) {
    console.log(`${key} : ${value}`);
}


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ La boucle for...in
/////////////////////////////////////////////////////////////////////////////////////////////
/* Une autre façon d'itérer sur un objet est d'utiliser la boucle "for" avec le mot-clé "in".
 * Contrairement à ce qui a été vu ci-dessus, ce mot-clé va permettre d'itérer sur les clés
 * d'un objet, nous laissant ainsi le soin d'accéder à la valeur correspondant à cette clé.
 */

const specs = {
    processor: "Ryzen 9",
    ram: 512,
    ssd: 256
};
// Pour chaque clé dans "specs"
for (const key in specs) {
    const value = specs[key];
    console.log(`${key} = ${value}`);
}


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ L'instruction switch
/////////////////////////////////////////////////////////////////////////////////////////////
/* Dans le cas où l'on veuille exécuter un bout de code en fonction de la valeur d'une
 * variable, l'instruction "switch" peut s'avérer utile en remplacement de plusieurs
 * "if" et "else if".
 * Voyons d'abord un exemple de "if" et "else if" que l'on veut écrire avec un "switch".
 */

const transport = "tramway";

if (transport == "train") {
    console.log("Vous pouvez venir à l'aide du RER A.");
} else if (transport == "tramway") {
    console.log("Le tramway 2 dessert le stade.");
} else if (transport == "metro") {
    console.log("La ligne 1 est à 10 minutes de marche du stade.");
}

/* On écrit l'instruction "switch" en précisant la variable dont on veut vérifier la valeur,
 * puis l'on écrit différents cas (case) selon les valeurs possibles.
 * Au sein de chaque cas, on écrit le code que l'on veut exécuter, suivis de
 * l'instruction "break" pour terminer le fonctionnement du "switch".
 */
switch (transport) {
    case "train":
        console.log("Vous pouvez venir à l'aide du RER A.");
        break;
    case "tramway":
        console.log("Le tramway 2 dessert le stade.");
        break;
    case "metro":
        console.log("La ligne 1 est à 10 minutes de marche du stade.");
        break;
}

/* La particularité (et la difficulté) du bloc "switch" est que, dès qu'il rencontre un cas
 * où la valeur est égale à la variable testée, il va exécuter le code correspondant
 * à ce cas ET tous le code des cas suivants. Vu que c'est un comportement que l'on veut
 * en général éviter, c'est pour cela que l'on rajoute l'instruction "break".
 * Cependant, lorsque l'on souhaite ce comportement, on peut retirer le "break" voire
 * retirer le contenu d'un cas afin d'exécuter le même code pour plusieurs cas.
 */

switch (transport) {
    case "train":
    case "tramway":
    case "metro":
        console.log("Vous venez en transports en commun.");
        break;
    case "voiture":
    case "moto":
        console.log("Vous venez en transports personnel.");
        break;
}
