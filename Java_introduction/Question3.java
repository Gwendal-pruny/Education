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
