
# Exercice "Journal"

![Logo](../../assets/journal.png)

👉 À réaliser après avoir lu le cours "Intermédiaire 1"

## 📜 Situation

Le quotidien pour lequel vous travaillez, Le Lutécien, a besoin de connaître rapidement les articles devant paraître dans le prochain journal avant envoi à l'imprimeur.

Chaque journal peut inclure des articles d'actualité ainsi que des interviews, dont certains peuvent être réservés à une édition régionale. Les articles/interviews destinés à l'édition nationale paraissent cependant aussi dans les éditions régionales.

Pour l'instant, le journal n'a que deux éditions régionales en Ile-de-France et au PACA.

## 🏁 Objectifs

Le premier but est d'utiliser, de façon simple, des classes pour représenter des données : dans notre cas, des articles et des interviews. L'intérêt premier de la programmation orienté objet est de pouvoir éviter de la duplication de code en ayant une classe "parent" qui contiennent des choses communes, puis des classes "enfant" qui héritent de cette dernière pour y ajouter des choses spécifiques.

Pour commencer, à vous de récupérer la liste des articles et interviews. Ils sont répartis en deux listes, dans le module `donnees.py`, qu'il vous faudra donc importer dans le fichier `journal.py`. Pour l'instant, on va rester simple au niveau des dates : ce sont toutes des `str` sous la forme "annee-mois-jour", par exemple `2021-04-01`.

Un héritage simple est déjà présent pour vous guider sur ce qu'il faudra y écrire pour les faire fonctionner, tout en gardant l'aspect polymorphe.

Les classes `Article` et `Interview` vous serviront à créer une instance de l'une ou de l'autre afin de représenter les données brutes de `donnees.py`. Un intérêt de l'héritage de classes étant d'éviter la duplication de code, la classe `ElementJournal` devra contenir les choses qui se trouvent autant dans un article que dans un interview (date...). Ensuite, il faudra rajouter les champs qui sont uniques aux articles à la classe `Article`, et les champs uniques aux interviews à la classe `Interview`.

La classe `Generateur` est le coeur du script. Tout d'abord, elle est instanciée en précisant la date et l'édition du journal voulu selon ce qui a été écrit dans le terminal (et récupéré grâce à `argparse`).

Ensuite, on appelle sa fonction `importer()` en passant les données brutes importées au préalable du module `donnees.py`. En parcourant chacune de ces listes de dictionnaires, il faudra instancier au choix la classe `Article` ou `Interview` tout en leur passant les données dans le bon sens, selon comment ont été écrit les constructeurs des classes `Articles` et `Interview`. Une fois l'instance créée, vous pourrez par exemple la stocker dans une liste unique.

Lorsqu'une classe est instanciée, elle remplit généralement ses propriétés grâce à ce qu'elle reçoit dans son constructeur. C'est à vous de coder, dans les classes, les constructeurs `__init__` qui vont recevoir les données passées lors de l'instanciation, afin de remplir les propriétés de la classe.

Ensuite, en parcourant la liste contenant les instances de classes, vous devrez déterminer si une instance provient de `Article` ou de `Interview` afin de savoir quelles propriétés utiliser dessus pour afficher leur contenu. Bien sûr, il ne faudra afficher dans le terminal que les articles et interviews correspondant à la date et à l'édition qui ont été passés comme arguments lors de l'appel du script.

Notre script peut accepter et comprendre des arguments lors de son appel dans une ligne de commande, grâce à l'usage de la bibliothèque `argparse`. Le script attends comme premier argument une date (au format annee-mois-jour) puis une édition ("national", "paca"...). Écrire par exemple `python journal.py 2021-01-06 paca` devra générer le journal dans on édition PACA pour le 2 Avril 2021. Vous pouvez écrire `python journal.py --help` pour plus de détails.

## ☝ Conseils

Le plus simple pour décider de quels éléments à afficher ou non selon une édition de journal est peut-être de déterminer à l'avance les éditions desquelles on accepte les articles et interviews.

La lisibilité des caractéristiques et du contenu des articles/interviews est évidemment importante, n'hésitez pas à les écrire sur plusieurs lignes.
