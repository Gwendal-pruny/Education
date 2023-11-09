import requests
import argparse

# L'adresse du site web proposant l'API que l'on veut appeler
basepath = "http://localhost:8000"

def get_articles(): 
    print("Get all articles IDs -> GET request on /api/articles")

    # Requête GET sur l'endpoint /api/articles
    req = requests.get(basepath + "/api/articles")
    # Récupère la réponse en désérialisant le JSON vers une valeur Python
    response = req.json()

    print("Response :")
    print(response["articles_ids"])

def post_articles():
    print("Create a new article -> POST request on /api/articles")

    request_body = {
        "slug": "",
        "data": "2021-06-01",
        "edition": "national",
        "auteur": "",
        "titre": "",
        "contenu": ""
    }

    # Requête POST sur l'endpoint /api/articles avec un corps de requête (data)
    req = requests.post(basepath + "/api/articles", data=request_body)
    # Récupère la réponse en désérialisant le JSON vers une valeur Python
    response = req.json()

    if "error" in response:
        print("/!\ Error : " + response['error'])
        return

    print("Response :")
    print(response)

def delete_article(article_id): 
    print(f"Delete an article -> DELETE request on /api/article/{article_id}")

    # Requête DELETE sur l'endpoint /api/article/id
    req = requests.delete(basepath + f"/api/articles/{article_id}")
    # Récupère la réponse en désérialisant le JSON vers une valeur Python
    response = req.json()

    print("Response :")
    print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Permet de tester les endpoints API du projet Minimal News")
    parser.add_argument("fonction", help="Fonction Python à appeler")
    args = parser.parse_args()

    if args.fonction == "get-articles":
        get_articles()
    elif args.fonction == "post-articles":
        post_articles()
    elif args.fonction == "delete-article":
        delete_article(4)
    else:
        print("Méthode inconnue.")
