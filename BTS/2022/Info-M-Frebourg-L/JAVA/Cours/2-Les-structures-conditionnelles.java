// Indiquer si un nombre est supérieur à 30.

class Question4 {
    public static void main(String[] args) {
        int x = 12;
        if (x > 30) {
            System.out.println("x est supérieur a 30");
        } else {
            System.out.println("x est inférieur a 30");
        }
    }
}

// ’entreprise accorde une remise de 10 % sur le prix TTC pour tout achat de plus de 100 pièces ; écrire le programme calculant le prix TTC en fonction de la quantité, du prix HT et du taux de TVA.

import java.util.Scanner;
class Question5 {
    public static void main(String[] args) {
        double prixTTC= 0;
        int prixHT= 0;
        double TVA= 0.1;
        int Quantity= 3;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de votre article :");
        prixHT = sc.nextInt();
        prixTTC= (prixHT*(1+TVA)*Quantity);

        if (prixHT > 100 ) {
            System.out.println((prixTTC*0.10)+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(prixTTC);
        }
    }
}

//Une agence de voyage propose des réductions sur les billets d’avion de 50€ selon la catégorie de chacun de ses clients.
//Si les personnes sont dans la catégorie senior, ils ont 50% de réductions.
//Dans la catégorie nourrisson, le prix du billet est forfaitaire, il sera de 20 euros.
//Pour les enfants, le prix sera de 30% de celui d’origine.
//Écrire le programme qui affiche le prix final pour un client.


import java.util.Scanner;
class Question6 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Billet pour un : senior, nourrisson, ou enfants ?");
        double prix;
        String categorie;
        categorie = sc.nextLine();
        switch (categorie) {
            case "senior":prix = 25;
                break;
            case "nourrisson" :prix = 20;
                break;
            case "enfants":prix = (50*0.30);
                break;
            default:
                prix = 0;
                System.out.println("Erreur : Merci de choisir entre senior, nourrisson, enfants");
                break;
        }
        System.out.println("Le prix est de " + (prix));
    }
}