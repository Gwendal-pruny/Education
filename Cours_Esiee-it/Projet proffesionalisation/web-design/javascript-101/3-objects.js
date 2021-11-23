/*
 * JavaScript 101
 * (3) Objets
 * 🔨 Créer un objet
 * 🔨 Manipuler une chaîne de caractères
 * 🔨 ️Manipuler une liste
 * 🔨 ️Manipuler un objet
 */


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 Créer un objet
/////////////////////////////////////////////////////////////////////////////////////////////
/* Comme vu précédemment, un objet Javascript se crée assez simplement à l'aide d'accolades
 * dans lesquels nous écrivons des paires de valeurs associées à des propriétés (clés).
 * Les valeurs peuvent d'être de tout type, faire référence à des variables existantes, etc.
 */
const roles = ["Utilisateur", "Administrateur"];

const user = {
    email_address: "test@example.com",
    age: 25,
    role: roles[0]
};


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 Manipuler une chaîne de caractères
/////////////////////////////////////////////////////////////////////////////////////////////
/* On peut modifier une chaîne de caractères de différentes façons grâce à de nombreuses
 * fonctions disponibles dessus :
 *     .indexOf(string) pour avoir la position d'une chaîne, si elle y est présente
 *     .replace(ancien, nouveau) pour remplacer un bout de chaîne par une autre
 *     .toUpperCase() pour passer son contenu en majuscules
 *     .toLowerCase() pour passer son contenu en minuscules
  *    .split(separateur) pour découper une chaîne et la transformer en liste
 */

console.log("Navigation vers le Grand Palais".indexOf("Grand Palais"));
console.log("Ce soir : pluie".replace("pluie", "neige"));
console.log("un,deux,trois".split(","));
console.log("bonjour à TOUS".toUpperCase());
console.log("BONSOIR TOUT LE monde".toLowerCase());


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 ️Manipuler une liste
/////////////////////////////////////////////////////////////////////////////////////////////
/* Les listes ont également leur lot de méthodes permettant d'en modifier le contenu.
 */
let food = ["Ramen", "Gyudon", "Soba"];

// La méthode .push(el) ajoute un élément à la fin du tableau
food.push("Udon");
console.log(food);

// La méthode .unshift(el) va au contraire ajouter l'élément au début du tableau
food.unshift("Onigiri");
console.log(food);

// La méthode .pop() va à la fois supprimer le dernier élément du tableau, et le retourner
const lastItem = food.pop();
console.log(lastItem);
console.log(food);

// La méthode .shift() fera la même chose mais avec le premier élément du tableau
const firstItem = food.shift();
console.log(firstItem);
console.log(food);

/* La méthode .splice(debut, nb) va supprimer le nombre d'éléments voulus à partir de l'index
 * passé comme premier argument. Préciser "1" élément va donc supprimer l'élément situé
 * directement à cet index. La méthode renvoie un tableau contenant les éléments supprimés.
 */
const removedItem = food.splice(1, 1);
console.log(removedItem);
console.log(food);


/////////////////////////////////////////////////////////////////////////////////////////////
// 🔨 ️Manipuler un objet
/////////////////////////////////////////////////////////////////////////////////////////////
/* La manipulation des objets n'est pas bien compliquée, car elle s'apparente à la
 * simple manipulation de variables.
 */
const pizza = {
    nom: "Margherita",
    ingredients: [
        "tomates",
        "mozzarella"
    ],
    supplement: "fromage",
    pate: "classique"
}

// La valeur d'un objet se remplace comme avec une variable
pizza.pate = "fine";
console.log(pizza);

// Exemple de modification d'un tableau présent dans l'objet
pizza.ingredients.push("basilic");
console.log(pizza);

// La suppression d'une valeur se fait également comme la suppression d'une variable
delete pizza.supplement;
console.log(pizza);
