
import java.util.Scanner;

class TinyCar3 {
    public static void main(String[] args) {
        
        // On initialise toutes les variables
        double TVA= 0.20;
        int Quantity= 3;
        double Reduc= 0;
        boolean isValid= false;
        String categorie;

        while(!isValid) {

            Scanner sc = new Scanner(System.in);
            //MDP
            System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
            int mdp = sc.nextInt();
            if (mdp != 42){
                System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
            }
            sc = new Scanner(System.in);
            // get carde info
            System.out.println("Veuillez indiquer si vous possèder une carte de fiddeliter : [oui/non]");
            String carte = sc.nextLine();
            // apply advantage for vip
            if (carte == "oui"){
                System.out.println("Veuillez indiquer ca gamme : [gold/platinium]");
                categorie = sc.nextLine();
            }
            else {
                categorie = null;
            }
            sc = new Scanner(System.in);
            //get marque
            System.out.println("Veuillez saisir la marque :");
            String marque = sc.nextLine();
            sc = new Scanner(System.in);
            //get model
            System.out.println("Veuillez saisir le model :");
            String model = sc.nextLine();
            //get v type
            System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
            String elec = sc.nextLine();
            // apply reduc if v type is electrique 
            if (elec == "oui"){
                TVA = 5;
            }
            sc = new Scanner(System.in);
            // get v price
            System.out.println("Veuillez saisir le prix de la "+ (model)+"de marque"+ (marque)+ " :");
            int prixHT = sc.nextInt();
            //get price without reduce adventages
            double PrixTTC = (prixHT*(1+TVA)*Quantity);
            switch (categorie) {
                // apply reduc adventage of gold and plat member
                case "gold":Reduc = Reduc + 0.20;
                    if (elec == "oui"){
                        Reduc = Reduc + 10;
                    }
                    break;
                case "platinium" :Reduc =  Reduc + 15;
                    break;
                case "nul":Reduc = Reduc;
                    break;
                default:
                // invalide inpuit
                    System.out.println("404 - La carte de fideliter est invalide");
            }
            //apply overall reduce for 20k + car
            if (prixHT > 20000) {
                Reduc = Reduc + 10;
            }
            //get the final price
            double prix = PrixTTC*(Reduc/100);
            System.out.println("Votre voiture coute (TTC):"+(prix)+" (Felicitation vous avez une réduc de "+Reduc +"%");


            System.out.println("Voulez-vous recommancer ? oui / non ");
            String reload = sc.nextLine();
            if (reload == "oui") {

            }
            else {
                System.out.println("Merci, bonne journée");

            }
        }
    }
}
