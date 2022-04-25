// Donner le type des variables :

public class Question1 {
    public static void main (String[] args){
        int age=20; // int
        int i=0; // int
        int o=1+1; // int
        int j=i; // char
        String k="coucou";// string
        String h=k+k; // String
        boolean majeur=(age>18); // bool
    }

}

// Le code Java suivant ne fonctionne pas, pourquoi ?

//    Les varaibles ne sont pas déclarer



// Écrire le programme qui affiche le prix total TTC en fonction du prix HT,
// du taux de TVA et de la quantité achetée ( on prendra des valeurs au hasard).

public class Question3 {
    public static void main (String[] args){
        double prixTTC;
        prixTTC= 0;
        int prixHT= 100;
        double TVA= 0.10;
        int Quantity= 3;
        prixTTC= (prixHT*(1+TVA)*Quantity);

        System.out.println(prixTTC);
    }
}

// Écrire un programme qui initialise deux variables entières et qui affiche directement la somme de ces deux nombres.
// N’oubliez pas d’afficher un message à l’utilisateur pour qu’il sache quoi saisir.

import java.util.Scanner;
class Question4 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le premier nombre :");
        int a = sc.nextInt();
        System.out.println("Veuillez saisir le second nombre :");
        int b = sc.nextInt();
        System.out.println("Vous avez saisi : "+(a + b));
    }
}