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
