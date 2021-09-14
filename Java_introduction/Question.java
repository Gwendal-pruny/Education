//Question 1 : Donner le type des variables :

class Test{
    public static void main (String[] args){
        age=20; // int
        i=0; // int
        i=1+1; // int
        j=i; // char
        k=«coucou»; // string
        h=k+k; //char 
        majeur=(age>18); // bool
    }
}

// Question 2 : Le code Java suivant ne fonctionne pas, pourquoi ? ( Test2.java :5 :possible loss of precision ) 

class Test2{
    public static void main (String[] args){
        int ia; // double ia;
        double fa;
        fa=3.14;
        ia=3.14;
    }
}

// Question 3 : Écrire le programme qui affiche le prix total ttc 
// en fonction du prix ht, du taux de tva et de la quantité achetée ( on prendra des valeurs au hasard).

class Padawan{
    public static void main (String[] args){
        double prixTTC;
        prixTTC= 0;
        prixHT= 100;
        TVA= 0.10;
        Quantity= 3;
        PrixTTC= (PrixHT*(1*TVA)*Quantity);

        System.out.println(PrixTTC);
    }
}

//Question 4 : Écrire un programme qui initialise deux variables entières et qui affiche directement la somme de ces deux nombres.
// N’oubliez pas d’afficher un message à l’utilisateur pour qu’il sache quoi saisir.

import java.util.Scanner;

class Sawan{
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le premier nombre :");
        int a = sc.nextInt();
        System.out.println("Veuillez saisir le second nombre :");
        int b = sc.nextInt();
        System.out.println("Vous avez saisi : " (a + b);
    }
}

//Indiquer si un nombre est supérieur à 30.

class Padawan {
    public static void main(String[] args) {
        if (x > 30) {
            System.out.println("x est  superieur a 30 ");
        } else {
            System.out.println("x est inferieur a 30");
        }
    }
}

//L’entreprise accorde une remise de 10 % sur le prix ttc pour tout achat de plus de 100 pièces ;
//écrire le programme calculant le prix ttc en fonction de la quantité, du prix ht et du taux de tva.

//import java.util.Scanner;
class Padawan {
    public static void main(String[] args) {
        double prixTTC;
        prixTTC= 0;
        prixHT= 0;
        TVA= 0.1;
        Quantity= 3;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de votre article :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1*TVA)*Quantity);

        if (prixHT > 100 ) {
            System.out.println((PrixTTC*0.10)+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}


// Une agence de voyage propose des réductions sur les billets d’avion de 50€
// selon la catégorie de chacun de ses clients. Si les personnes sont dans la catégorie senior, ils ont 50%
// de réductions. Dans la catégorie nourrisson, le prix du billet est forfaitaire, il sera de 20 euros. Pour les enfants, le prix sera de 30% de celui d’origine.
// Écrire le programme qui affiche le prix final pour un client.

// import java.util.Scanner;

class Padawan {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Billet pour un : senior, nourrisson, ou enfants ?");
        int prix;
        String categorie;
        categorie = sc.nextString();
        switch (categorie) {
            case "senior":prix = 25;
                break;
            case "nourrisson" :prix = 20;
                break;
            case "enfants":prix = (50*0.30);
                break;
            default:
                System.out.println("Erreur : Merci de choisir entre senior, nourrisson, enfants");
                stop;
        }
        System.out.println("Le prix est de " + prix);
    }
}

//Écrire un programme qui saisit deux entiers et qui incrémente de 1 le premier tant qu’il n’est pas supérieur au deuxième.

//import java.util.Scanner;

class Padawan{
    public static void main (String[] args){
        Scanner sc=new Scanner(Sytem.in);
        double num,den;
        num=sc.nextDouble("entrez le premier nombre");
        do{
            den=sc.nextDouble("entrez le denominateur");
        }
        while(num < den){
            num = (num+1)
        };
    }
}

//Afficher les nombres pairs de 0 à 20 dans l’ordre décroissant

for (int indice = 20; indice >= 0; indice--) {
    System.out.print(indice);
}

//Que fait cette boucle ?

//Tant que indice est >= 0 on retire 2 a indice et on l'imprime 

//Afficher pour chaque nombre de 1 à 10 les nombres qui lui précédent .

class Padawan {
    public static void main(String[] args) {
        
        int mainnombre = 1;
        int nombre = 0:

        for (mainnombre <= 10) {
            nombre = mainnumbre;
            for (nombre > 0; nombre+){
                System.out.println(nombre);
            }
            mainnumber = mainnumber + 1
        }
    }
}

// 1.Écrire un programme qui saisit un entier positif.                                          //boucle et fonction c'est chiant et long. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! a faire 
// 2.Écrire un programme qui affiche n fois ‘coucou’, l’entier n sera saisi par l’utilisateur.
// 3.Écrire un programme qui saisit un nombre tant qu’il n’est pas égal à 10.
// 4.Écrire un programme qui saisit un nombre tant qu’il n’est pas égal à 10 et affiche un message du style ‘ce nombre n’est pas bon’.

// Écrire une fonction afficherPersonne qui prend en paramètre le prénom et affiche le nom et le prénom de la personne. Le nom est déclaré en variable globale.
// Ecrire la fonction principale qui utilise votre fonction.
// Ecrire une fonction qui affiche la somme de trois nombres passés en paramètre.
// Ecrire une fonction qui renvoie la soustraction de deux nombres
// Ecrire une fonction qui ajoute 7 nombres saisis par l’utilisateur à un nombre passé en paramètre et le renvoie.

///////////////////////////

// Modifier le programme précédent pour qu’il puisse créer deux autres objets p3 et p4.
// Réaliser une classe Sandwich qui possède comme propriété trois ingrédients, un poids et un prix.

public void affiche(){
    System.out.println(nom+" "+annee_naissance);
    }
public void calcul_age(){
    int age=2011-annee_naissance;
    System.out.println("age = "+age);
}
    --------------------------------------------------------------------------------------------------------
public static void main(String args[]){
    Sandwich ingredients1=new ("dupont",1950);
    Personne ingredients2=new Personne("mercier",1962);
    Personne ingredients3=new Personne("mercier",1962);
    Personne prix=new Personne("mercier",1962);
    System.out.println(p1.nom);
    p1.affiche();
    p2.affiche();
    p3.calcul_age();
    p4.calcul_age();
}