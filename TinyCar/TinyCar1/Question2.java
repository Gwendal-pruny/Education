package TinyCar1;
class Question2{
    public static void main (String[] args){
        double prixTTC;
        int prixHT= 100;
        double TVA= 0.10;
        int Quantity= 3;
        prixTTC= (prixHT*(1+TVA)*Quantity);

        System.out.println(prixTTC);
    }
}