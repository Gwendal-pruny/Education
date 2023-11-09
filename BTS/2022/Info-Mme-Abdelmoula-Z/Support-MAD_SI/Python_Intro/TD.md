
ESIEE-IT
BTS SIO 1er semestre
Initiation à la programmation avec Python
Année universitaire 2021-2022
Dr. Nourhène Ben Rabah




TD1 : Prise en main de Python (ce qui n’est pas terminé en TD doit être terminé à la maison)




L'objectif de ce TP est d’expliquer les principaux concepts du langage Python. Pensez à remplir votre compte-rendu au fur et à mesure pendant la séance.

Exercice 1
Que font les extraits de code suivants (sans exécuter) ?

    (a) j=input("saisir un nombre :") a=type(j)
print (a)

    (b) ch="aaabbb" print(type(ch)) a=1.2 print(type(a))

    (c) a=int(input()) print(type(a))

    (d) a=input('Saisissiez svp un entier') print (a)
print(type(a))

Exercice 2
        2.1 Réalisez les trois affectations de variables suivantes en Python : a = 7
mot = ”Bonjour” x = 1.234
        2.2 Quel est le type de chaque variable ?
        2.3 Tentez de convertir mot en entier, avec la fonction int(). Que se passe-t-il ?
        2.4 Assignez la variable a à x. Que devient le type de x ? Incrémentez x et vérifiez les valeurs obtenues pour x et a.

Exercice 3
Exécuter les codes suivants, quelles différences observez-vous ?
            ▪ print ("Bonjour tout le monde")
            ▪ print ("Bonjour", "tout", "le", "monde", sep="-")
            ▪ print ("Bonjour", "tout", "le", "monde", sep=" ")
            ▪ print ("Bonjour"); print ("tout le monde")
            ▪ print ("Bonjour", end=" "); print ("tout le monde")


            ▪ p=input("Qui est tu? >>> "); print("Bonjour"); p
            ▪ p=input("Qui est tu? >>> "); print("Bonjour", p)


            ▪ print ("Je sais que c’est pas vrai mais j’ai 8 ans")
            ▪ print ("Je sais que c’est pas vrai mais j’ai", 8, "ans")
            ▪ i=8; print ("Je sais que c’est pas vrai mais j’ai", i, "ans")
            ▪ j=12; print ("Je sais que c’est pas vrai mais j’ai %d ans" %(j))


            ▪ i=8 ; j=12 print("i et j valent respectivement %d et %d" ,%(i, j))
-	print("%d/%d=%d" %(i, j, i/j))
-	print("%d/%d=%f"%(i,j,i/j))


            ▪ type(p)
            ▪ type(i)
            ▪ type(j)
            ▪ type(i/j)
-	n=12/8 ; n
-	n=int(12/8) ; n

Note:
%d - Entiers
%s - Chaîne (ou tout objet avec une représentation en chaîne, comme les nombres)
%f - Chiffres à virgule flottante

Exercice 4
Un environnement de développement intégré, ou IDE, est un logiciel de création d'applications, qui rassemble des outils de développement fréquemment utilisés dans une seule interface utilisateur graphique (GUI).

Installez et configurez l’EDI PyCharm Community Edition. Vous pouvez se baser sur ce lien : http://python-liesse.enseeiht.fr/cours/outils.html