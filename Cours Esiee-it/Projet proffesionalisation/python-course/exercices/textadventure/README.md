
# Exercice "Text Adventure"

![Logo](../../assets/auacademy.png)

👉 À réaliser après avoir lu le cours "Introduction 2"

## 📜 Situation

Un manga très en vogue désire être adapté en jeu vidéo par son comité de production. Afin de valider les idées de gameplay, le ton des dialogues, et pour récapituler rapidement tout ce que l'on pourra faire dans le jeu, le studio mandaté a décidé de réaliser un prototype sous forme de jeu textuel qui se joue dans le terminal.

Dans le scénario du manga, le lycée A.U. vise à former les meilleurs héros des pays où il se trouve. Son nom vient de la prononciation des lettres "AU" en anglais qui est semblable à la prononciation de "héros" en japonais, qui se dit "eiyuu". Toute référence à un autre lycée n'est que fortuite...

L'action du jeu se passe donc dans ce lycée. Après avoir rempli un questionnaire au début du jeu pour créer le personnage principal, le joueur peut se déplacer librement dans différents endroits du lycée, chacune proposant des actions que l'on peut réaliser.

## 🏁 Objectifs

Les fondations du jeu sont posées, mais il reste encore beaucoup à faire : les lieux à créer pour y accéder et pour y réaliser des actions, et surtout la salle d'entraînement où l'on peut se combattre de façon assez rudimentaire.

Cette fois-ci, il faudra autant lire des variables que les manipuler, selon les actions réalisées par l'utilisateur. Il n'y a que deux choses que l'utilisateur peut entrer : le nom d'un autre **lieu** vers lequel se déplacer, ou le nom d'une **action**.

Bien sûr, au delà d'avoir un code fonctionnel, l'objectif est de réussir à s'amuser un peu. Pour cela, n'hésitez pas à rajouter votre touche d'originalité à travers les dialogues, les actions réalisables, voire en rajoutant des lieux ou des fonctionnalités au jeu. Si une idée supplémentaire que vous tenez absolument à réaliser vous semble trop difficile, vous pouvez bien sûr me demander conseil.

### ● Gestion des objets

Le jeu commence avec la présence d'un smartphone comme **objet clé** (qui ne sert à rien de spécial) puis avec un **inventaire** vide.

Les objets clés n'ayant toujours qu'un seul exemplaire, on utilise une liste pour les stocker.

L'inventaire permet cependant de garder plusieurs quantités d'un même objet, on utilise alors un dictionnaire pour stocker la quantité au nom d'un objet.

Les deux types d'objets pourront servir tout au long du jeu. On peut récupérer des objets selon les endroits visités ou les actions réalisées.

### ● Les lieux

Pour être complet, le jeu doit proposer au minimum les lieux suivants :

* Hall d'entrée
* Couloir du 1er étage
* Classe 1-A (1er étage)
* Couloir du 2e étage
* Caféteria (2e étage)
* Salle d'entraînement (2e étage)

On ne peut aller d'un lieu à un autre que si l'on y est proche (du couloir du 1er étage à la classe 1-A par exemple). On ne peut pas rentrer dans la salle d'entraînement sans avoir un passe.

### ● Les actions

Une action prends la forme d'un verbe à l'infinitif. Vu que le jeu est textuel, il faudra être très descriptif en échange : une action commune à tous les lieux est donc `observer`.

Le hall, en particulier, possède l'action `quitter` qui arrête le script.

La cafétéria doit proposer l'action `manger`. Après avoir demandé le plat voulu, le joueur gagne 10 PV (points de vie). Il n'y a que 2 exemplaires de chaque plat en stock, il faudra donc **soustraire** un plat en stock à chaque utilisation, et **annuler** l'action quand un plat demandé n'est plus en stock.

Dans la classe 1-A, il doit y avoir l'action `demander`. En parlant au professeur, il vous donnera le passe (un objet clé) qui vous permettra d'entrer dans la salle d'entraînement du 2e étage. Il faut aussi prévoir l'action `montrer` qui sert à montrer au professeur le nombre de badges que l'on a sur soi : si on en a trois, le jeu est réussi et le script s'arrête.

Ainsi, dans la salle d'entraînement, l'action `combattre` lancera une **boucle** qui continuera tant que le mannequin d'entraînement n'aura pas ses PV à zéro. Au début d'un combat, le mannequin commencera toujours à 50 PV, qu'importe ce qu'il s'est passé auparavant. Dans cette boucle, il faudra proposer à l'utilisateur soit l'action `fuir` qui **annule** la boucle, soit l'action `attaquer`. L'attaque retire 15 PV au mannequin, et ce dernier répliquera en retirant 10 PV au joueur. Si le joueur perds tous ses PV, le script s'arrête. Au contraire, quand le mannequin est combattu avec succès, on gagne dans notre inventaire un **badge** qui atteste de notre réussite.

## ⭕ Conditions de réussite

- ✔️ On peut créer notre personnage puis voir le récapitulatif de ce dernier
- ✔️ On peut `observer` dans chaque lieu
- ✔️ On peut `manger` au maximum 2 exemplaires de chaque plat à la cafétéria, et ces derniers augmentent nos points de vie
- ✔️ On peut `demander` le passe au professeur dans la classe 1-A, mais si on l'a déjà, on peut lui montrer nos badges
- ✔️ On peut `combattre` contre un mannequin dans la salle d'entraînement
- ✔️ Le jeu s'arrête sur un game over si nos points de vie tombent à zéro lors d'un combat
- ✔️ Le jeu s'arrête sur une réussite si l'on montre 3 badges au professeur dans la classe 1-A

## ☝ Conseils

On travaille encore avec des variables globales afin de garder l'exercice relativement simple, bien que ça ne soit pas une pratique ni recommandée ni courante dans des projets Python concrets. Cependant, les variables globales ayant un type immutable ne peuvent pas voir leur valeur modifiée au sein d'une fonction. Je vous conseille donc de **n'utiliser que des listes et des dictionnaires** comme variables globales. Si vous souhaitez créer de nouvelles variables pour stocker des données en rapport avec le comportement de votre jeu, vous pouvez par exemple utiliser un même dictionnaire.

Plutôt que des nombres, on va souvent demander à l'utilisateur d'entrer du texte. Pour facilement comparer ce qui est écrit avec ce que l'on peut attendre, on peut peut-être uniformiser le texte écrit d'une façon ou d'une autre avec les fonctions built-in sur les `str`...

L'usage des fonctions permet théoriquement de réduire le plus possible le code dupliqué, mais c'est à vous de décider comment vous allez vous y prendre. Il faut surtout trouver le bon équilibre pour garder un code lisible, car cela reste le plus important.
