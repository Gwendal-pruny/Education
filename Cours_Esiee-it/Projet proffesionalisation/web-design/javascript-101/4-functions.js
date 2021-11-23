/*
 * JavaScript 101
 * (4) Fonctions
 * ️🖊️ Les fonctions
 * ⚙️ Le passage des variables
 * ⚙️ La portée des variables
 * 🖊️ Le déballage de valeurs
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Les fonctions
/////////////////////////////////////////////////////////////////////////////////////////////
/* Outil majeur pour découper son code en morceaux réutilisables, les fonctions permettent
 * de réaliser des tâches précises. Elles peuvent aussi accepter des valeurs que l'on
 * appellera alors "arguments", et elles peuvent renvoyer ou non une ou plusieurs valeurs.
 */


// Fonction standard
/* La première façon de déclarer une fonction est à l'aide du mot-clé "function" suivi
 * du nom de notre fonction. Entre les parenthèses, s'écriront les arguments que l'on voudra
 * accepter lors de l'appel de notre fonction.
 * "this" fera référence au scope global lorsqu'il est utilisé au sein de la fonction.
 */

// crée son scope et this est égal au scope supérieur
function standardFunc(message) {
    console.log(message);
}
standardFunc("Hello world !");

/* Les fonctions peuvent donc renvoyer une valeur si nécessaire à l'aide du mot-clé "return".
 * Tout code situé après ce mot-clé ne sera jamais exécuté.
 */
function returnSomething(name) {
    return "Hello " + name;
}
console.log(returnSomething("Mario"));

// Fonction fléchée
/* La seconde façon de déclarer une fonction rend son nommage optionnel, et utilise une
 * "flèche" pour la définir. On va donc généralement la stocker dans une variable, mais il est
 * très fréquent de passer une fonction fléchée comme argument lors de l'appel d'une fonction.
 */
const anonymousFunc = (a, b) => {
    console.log(a + b);
};
anonymousFunc(5, 10);

// Si une fonction anonyme n'attend qu'un seul argument, on peut omettre les parenthèses.
const oneArgument = message => {
    console.log(message);
};
oneArgument("Bonjour monde !");

/* Aussi, lorsqu'une fonction ne fait que directement renvoyer une valeur à l'aide d'une seule
 * ligne, on peut omettre les accolades et le mot-clé "return".
*/
const implicitReturn = () => 400 + 4;
console.log(implicitReturn());

// fonction passée comme argument


/////////////////////////////////////////////////////////////////////////////////////////////
// ⚙️ Le passage des variables
/////////////////////////////////////////////////////////////////////////////////////////////
/* En Javascript, toute valeur étant d'un type primitif (donc tout sauf les objets) sont
 * passées "par valeur" lorsque utilisées comme arguments lors de l'appel d'une fonction.
 */

const cannotEditString = (message) => {
    message = "no";
}
let message = "yes";
cannotEditString(message);
console.log(message); // => yes

/* Cependant, tout objet (et assimilés comme les listes) sont passées "par référence" :
 * toute modification au sein d'une fonction sera alors répercutée sur l'objet d'origine
 */
let pizzaReine = {
    sauce: "tomate"
}
const changeSauce = (pizza) => {
    pizza.sauce = "blanche";
}
changeSauce(pizzaReine);
console.log(pizzaReine);

let ingredients = ["champignons"];
const addGruyere = (items) => {
    items.push("gruyère");
}
addGruyere(ingredients);
console.log(ingredients);


/////////////////////////////////////////////////////////////////////////////////////////////
// ⚙️ La portée des variables
/////////////////////////////////////////////////////////////////////////////////////////////
/* Avec l'usage des fonctions apparaît un nouveau concept de JavaScript : 
 * la "portée" des variables. Par défaut, une variable est définie dans le scope (portée)
 * global. Il existe cependant des choses qui vont créer leur propre scope local :
 *     - Les structures conditionnelles if...
 *     - Les boucles for, while...
 *     - Les fonctions
 *     - Les classes
 */
let age = 25;
if (age > 20) {
    console.log(age); // => 25
    age = 10;
}
console.log(age); // => 10

/* Attention, attribuer une valeur à une variable encore non-existante va automatiquement la
 * créer dans le scope global. N'oubliez donc jamais le mot-clé "const" ou "let", qui feront
 * en sorte que toute variable définie dans un scope local ne sera alors pas accessible dans
 * le scope "supérieur", comme par exemple le scope global.
 */
function globalDemo() {
    itsGlobal = true;
}
globalDemo();
console.log(itsGlobal);

/* Tout ce qui est défini dans un scope est également accessible dans les scopes locaux
 * qui sont créés en son sein. Le principe des scopes est ce qui permet aux langages d'avoir
 * des variables portant le même nom mais ne se mélangeant pas : si vous voulez accéder à la
 * variable "a", le langage va d'abord vérifier son existence ou non dans le scope local.
 * Si la variable existe, vous en aurez sa valeur, sinon, le langage ira vérifier son
 * existence dans le scope parent, etc, jusqu'à arriver au scope global.
 */

let a = 25;
function fonction_x(a) {
    console.log(a); // => 42
    const b = 77;
}
fonction_x(42);
console.log(a); // => 25
// => b is not defined


/////////////////////////////////////////////////////////////////////////////////////////////
// 🖊️ Le déballage de valeurs
/////////////////////////////////////////////////////////////////////////////////////////////
/* Imaginons que l'on souhaite, pour avoir des noms plus explicites, attributer le contenu
 * d'un tableau à des variables. Pour l'instant, on ferait comme ceci :
 */
const userData = ["test@example.com", "administrateur", "paris"];

const email = userData[0];
const status = userData[1];
const localisation = userData[2];

/* Pour raccourcir cette opération, il est possible de réaliser ce qu'on appelle une
 * décomposition des valeurs pour extraire en un coup les valeurs d'un tableau dans plusieurs
 * variables.
 */

const [ firstname, lastname, birthdate ] = ["John", "DOE", "02/05/1989"];
console.log(lastname); // => DOE
