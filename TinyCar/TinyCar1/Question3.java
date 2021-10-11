package TinyCar1;
import java.util.Scanner;
class Question3 {
    public static void main(String[] args) {
        double TVA= 1.19;
        int Quantity= 1;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de votre article :");
        int prixHT = sc.nextInt();
        double PrixTTC = (prixHT*TVA)*Quantity;

        if (prixHT > 100 ) {
            System.out.println((PrixTTC*(1-(10/100)))+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(PrixTTC);
        }
        sc.close();
    }
}
