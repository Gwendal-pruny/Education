
document.addEventListener("DOMContentLoaded", function() {

    /* Événements sur les icônes */
    const icons = document.querySelectorAll(".icon");

    for (icon of icons) {
        icon.addEventListener("mousedown", function(event) {
            if (event.button == 0) {
                this.classList.add("shaking");
            }
        });
        icon.addEventListener("mouseup", function() {
            this.classList.remove("shaking");
        });
    }
    
    /* Événement sur le bouton */
    let howManyClicks = 0;
    const buttonTest = document.querySelector("#test");
    const nbClicksDiv = document.querySelector("#nb-clicks");

    buttonTest.addEventListener("click", function() {
        howManyClicks++;
        nbClicksDiv.innerText = howManyClicks;
    });

    
    /* Événements sur le champ texte */
    const gravureInput = document.querySelector("input[name='gravure']");
    const gravureParagraph = document.querySelector("#tablet-back p");

    const tabletDiv = document.querySelector("#tablet");
    const tabletBackDiv = document.querySelector("#tablet-back");

    gravureInput.addEventListener("focus", function() {
        tabletDiv.style.display = "none";
        tabletBackDiv.style.display = "block";
    });

    gravureInput.addEventListener("blur", function() {
        tabletDiv.style.display = "flex";
        tabletBackDiv.style.display = "none";
    });

    gravureInput.addEventListener("input", function() {
        const text = gravureInput.value;
        if (text.length > 0) {
            gravureParagraph.innerText = text;
        } else {
            gravureParagraph.innerText = "Votre gravure ici";
        }
    });
});
