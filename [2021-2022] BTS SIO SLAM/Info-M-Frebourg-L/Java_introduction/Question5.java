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