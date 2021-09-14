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
        System.out.println("Veuillez saisir un nombre :");
        int a = sc.nextInt();
        System.out.println("Vous avez saisi : " + a);
    }
}