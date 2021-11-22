package TinyCar3;

import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        double tva = 1.2;
        Scanner sc = new Scanner(System.in);
        System.out.println("c quoi ton choix");
        int nb = sc.nextInt();

        for (int n = 0; n < nb; n++) {
            System.out.println("Au revoir");

            System.out.println("Tapez le nom de la marque de la voiture");
            String vtmarque = sc.next();
            System.out.println("Tapez le nom du modèle de la voiture");
            String vtmodele = sc.next();
            System.out.println("Tapez le prix HT de la voiture");
            double prixht = sc.nextInt();

            double prixttc = prixht * tva;

            System.out.println("Modèle : " + vtmodele);
            System.out.println("Voici la Marque : " + vtmarque);

            if (prixttc > 20000) {

                double prixttcremise = prixttc * 0.9;
                System.out.println("Voici le prix avec la remise " + prixttcremise);
            } else {
                System.out.println("Voici le prix TTC  : " + prixttc);

            }
        }
    }
}