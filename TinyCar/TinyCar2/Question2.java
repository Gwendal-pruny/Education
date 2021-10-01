package TinyCar2;
import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        double TVA= 0.20;
        int Quantity= 3;


        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :");
        String marque = sc.nextLine();
        System.out.println("Veuillez saisir le model :");
        String model = sc.nextLine();
        System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
        String elec = sc.nextLine();
        if (elec == "oui"){
            TVA = 0.05;
        }
        System.out.println("Veuillez saisir le prix de la "+ (model)+"de marque"+ (marque) +" :");
        int prixHT = sc.nextInt();
        double PrixTTC= (prixHT*(1+TVA)*Quantity);

        if (prixHT > 20000 ) {
            System.out.println("Votre voiture coute (TTC):"+(PrixTTC*0.10)+ " (Felicitation vous avez bonne conscience ! vive tesla  ou pas...!)");
        } else {
            System.out.println(PrixTTC);
        }
    }
}
