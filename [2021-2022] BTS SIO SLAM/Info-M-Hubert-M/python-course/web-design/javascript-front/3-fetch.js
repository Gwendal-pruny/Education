
const baseUrl = "http://localhost:8000/api/";
const templateHtml = document.querySelector("#template");
const articlesContainer = document.querySelector("#articles");

function getArticlesIds() {
    fetch(baseUrl + "articles").then((response) => response.json()).then((data) => {
        for (const id of data.articles_ids) {
            getOneArticle(id);
        }
    }).catch((err) => {
        console.error(err);
        displayMessage(err);
    });
}

function getOneArticle(id) {
    fetch(baseUrl + "articles/" + id).then((response) => response.json()).then((data) => {
        displayArticle(data.article);
    }).catch((err) => {
        console.error(err);
        displayMessage(err);
    });
}

function displayArticle(article) {
    const articleHtml = templateHtml.cloneNode(true);
    articleHtml.removeAttribute("id");
    articleHtml.classList.remove("d-none");
    articleHtml.classList.add("edition-" + article.edition);

    articleHtml.querySelector("h3").innerText = article.titre;
    articleHtml.querySelector("span").innerText = `Écrit par ${article.auteur} - Edition ${article.edition}`;
    articleHtml.querySelector("p").innerText = article.contenu;

    articlesContainer.append(articleHtml);
}

function displayMessage(text) {
    const messageContainer = document.querySelector("#message");
    messageContainer.style.display = "block";
    messageContainer.innerHTML = text;
}

getArticlesIds();
