package TinyCar2;
import java.util.Scanner;

public class Question1 {
    public static void main(String[] args) {
        double TVA= 0.1;
        int Quantity= 1;


        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :");
        String marque = sc.nextLine();
        System.out.println("Veuillez saisir le model :");
        String model = sc.nextLine();
        System.out.println("Veuillez saisir le prix de la "+(model)+ " de marque"+(marque)+ " :");
        int prixHT = sc.nextInt();
        double PrixTTC = (prixHT*(1+TVA)*Quantity);

        if (prixHT > 20000 ) {
            System.out.println("Votre voiture coute (TTC):"+(PrixTTC-(PrixTTC*0.10))+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println("Votre voiture coute (TTC):"+(PrixTTC));
        }
        sc.close();
    }
}
