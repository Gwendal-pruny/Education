package TinyCar3;

import java.util.Scanner;

public class Question3 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            double tva;
            String mdp = "667";
            System.out.println("Tapez le mot de passe");
            String verif = sc.next();
            int i = 1;

            while (!verif.equals(mdp) && i < 3) {
                System.out.println("Réesayez");
                verif = sc.next();
                i++;
            }

            if (verif.equals(mdp)) {

                System.out.println("Bienvenue");
                System.out.println("Tapez le nom de la marque de la voiture");
                String vtmarque = sc.next();
                System.out.println("Tapez le nom du modèle de la voiture");
                String vtmodele = sc.next();
                System.out.println("Tapez le prix HT de la voiture");
                double prixht = sc.nextInt();
                System.out.println("Le véhicule est-il electrique ?");
                String type = sc.next();
                if (type.equals("oui")) {
                    tva = 1.05;
                } else {
                    tva = 1.2;

                }

                double prixttc = prixht * tva;

                System.out.println("Modèle : " + vtmodele);
                System.out.println("Voici la Marque : " + vtmarque);

                if (prixttc > 20000) {

                    double prixttcremise = prixttc * 0.9;
                    System.out.println("Voici le prix avec la remise " + prixttcremise);
                } else {
                    System.out.println("Voici le prix TTC  : " + prixttc);

                }
            } else {
                System.out.println("Mot de passe incorrect bonne journée");

            }
        }
    }
}