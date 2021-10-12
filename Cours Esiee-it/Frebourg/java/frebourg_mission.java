import java.util.Scanner;

public class frebourg_mission {
    public static boolean isValid = false;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double dividandeTOTAL = 0;

        while(!isValid) {
            double secu = 0.5;
            double mutuelle = 0.27;
            System.out.println("Merci d'indiquer le montant de votre hospitalisation :");
            Double prixHT = sc.nextDouble();
            double prixSecu = prixHT * secu;
            double prixMutuelle = prixHT * mutuelle;
            double diviande =   prixHT - (prixSecu + prixMutuelle);
            System.out.println("Votre sécuriter social prendra en charge :"+(prixSecu));
            System.out.println("Votre mutuelle prendra en charge :"+(prixMutuelle));
            System.out.println("Ajouter une autre hospitalisation : oui / non ");
            String restart = sc.next().trim().toUpperCase();
            if (restart == "OUI") {
                dividandeTOTAL = dividandeTOTAL + diviande;
                System.out.println("Votre reste à charge :"+(dividandeTOTAL)+" rttrtrtrtrt");
                isValid = false;

            }
            else {
                dividandeTOTAL = dividandeTOTAL + diviande;
                System.out.println("Votre reste à charge :"+(dividandeTOTAL));
                isValid = true;
            }

        }
    }
}

