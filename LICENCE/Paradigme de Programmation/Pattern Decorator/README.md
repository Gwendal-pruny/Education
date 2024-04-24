## Travaux Pratiques : Structure d'Arbre Binaire avec Singleton
# Objectif :
L'objectif de ce TP est de créer une structure d'arbre binaire en utilisant une classe récursive ArbreBinaire. L'arbre vide sera codé sous la forme d'une instance unique.
# Partie 1: Définition de la Classe ArbreBinaire1.

Création de la Classe :
    o Définissez une classe ArbreBinaire avec les attributs suivants :
        ▪ clef : un attribut de type Integer représentant la valeur du nœud.
        ▪ gauche et droite : des attributs de type ArbreBinaire représentant les sous-arbres gauche et droit respectivement.
Constructeurs :
    o Ajoutez un constructeur qui ne prend pas de paramètre et créé l’arbre vide avec une clefnull et des sous-arbres null.
Singleton pour l'Arbre Vide :
    o Ajoutez un attribut statique arbreVide de type ArbreBinaire qui représente l'instanceunique de l'arbre vide en utilisant le premier constructeur
Getters et setters :
    o Ajoutez les getters et les setters
Méthode creer :
    o Ajoutez la méthode créer qui retourne l’arbre videPartie 2: Test de l'Application1.
Création de l'Arbre :
    o Dans une classe principale (Main), créez une instance de ArbreBinaire représentant unarbre binaire vide.    
Insertion de Valeurs :
    o Utilisez la méthode d'insertion pour ajouter plusieurs valeurs à l'arbre.
Affichage de l'Arbre :
    o Utilisez la méthode d'affichage pour afficher l'arbre après l'insertion des valeurs.

# Partie 3: Opérations sur l'Arbre Binaire1.

Méthode estVide : cette méthode retourne Vrai ou Faux si l’arbre est vide2. Méthode taille : cette méthode retourne la taille de cet arbre (i.e le nombre de nœuds)

Méthode de Recherche :
    o Ajoutez une méthode rechercher pour rechercher une valeur donnée dans l'arbre. Laméthode doit retourner true si la valeur est présente, sinon false.