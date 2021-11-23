
function selectElements() {
    // Sélectionner un seul élément, par balise
    const title = document.querySelector("h1");

    // Sélectionner un seul élément, par ID
    const alert = document.querySelector("#top-message");

    console.log("La balise de #top-message est", alert.nodeName);

    // Sélectionner plusieurs éléments, par classe
    const messages = document.querySelectorAll(".message");
    
    for (element of messages) {
        // On peut sélectionner sur un élément, plutôt que sur toute la page (document)
        const messageParagraph = element.querySelector("p");
        // .innerText renvoie le contenu strictement textuel
        console.log(messageParagraph.innerText);
    }

    // Accès aux attributs data d'un élément HTML
    const dataAttributes = document.querySelector("#profile").dataset;
    console.log("Le nom est :", dataAttributes.name);
    console.log("L'âge est :", dataAttributes.age);

    const profileList = document.querySelector("#profile ul");
    // .innerHTML renvoie le contenu et la structure HTML
    console.log(profileList.innerHTML);
}

function editElement() {
    const title = document.querySelector("h1");
    title.innerText = "Twatter !";

    const alert = document.querySelector("#top-message");

    alert.id = "top-alert";

    alert.classList.remove("alert-info");
    alert.classList.add("alert-danger");
    alert.innerHTML = "<b>Erreur</b><hr>Quelque chose a planté...";
}

function editElementStyle() {
    const title = document.querySelector("#profile h3");

    // .style est un comme un dictionnaire de toutes les propriétés CSS existantes
    title.style.color = "white";

    // Toute propriété ayant un tiret en CSS n'en a pas en JavaScript
    // "background-color" devient "backgroundColor", etc
    title.style.backgroundColor = "#19aff6";
}

function createElement() {
    const image = document.createElement("img");
    image.src = "assets/favicon.png";
    // Rajoute l'élément après l'élément HTML sélectionné
    document.querySelector("#profile").after(image);

    const newMessage = document.createElement("div");
    newMessage.classList.add("message");

    const user = document.createElement("b");
    user.innerText = "Arnaud :";
    newMessage.appendChild(user);

    const paragraph = document.createElement("p");
    paragraph.innerText = "Il faudrait penser à allumer la clim...";
    newMessage.appendChild(paragraph);

    const list = document.querySelector("#list");
    list.appendChild(newMessage);
}

// Ouvrez les devtools de votre navigateur pour appeler au choix l'une des fonctions ci-dessus.

console.log(`Fonctions à appeler : 
selectElements();
editElement();
editElementStyle();
createElement()
`);
