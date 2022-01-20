package TinyCar2;
import java.util.Scanner;

class Question4 {
    public static boolean isValid = false;
    public static void main(String[] args) {    
        Scanner sc = new Scanner(System.in);
    
        while(!isValid) {
            // initialize variables
            double TVA= 0.20;
            int Quantity= 1;
            double Reduc = 0.0;
            String marque = "None";
            String categorie;
            //MDP
            System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
            int mdp = sc.nextInt();
            if (mdp != 42){
                System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
                sc.close();
                isValid = true; // stop the programme
            }

            System.out.println("Veuillez indiquer si vous possèder une carte de fiddeliter : [oui/non]");
            String carte = sc.next();
            // apply advantage for vip

            if (carte.equals("oui")){
                System.out.println("Veuillez indiquer ca gamme : [gold/platinium]");
                categorie = sc.next();
            }
            else {
                categorie = "null";
                System.out.println(carte);
            }
            //get marque
            System.out.println("Veuillez saisir la marque :");
            marque = sc.next();
            //get model
            System.out.println("Veuillez saisir le model :");
            String model = sc.next();
            //get v type
            System.out.println("Veuillez indiquer si le véhicule est electique : [oui/non] ");
            String elec = sc.next();
            // apply reduc if v type is electric 
            if (elec == "oui"){
                TVA = 0.05;
            }
            // get v price
            System.out.println("Veuillez saisir le prix de la "+ (model)+" de marque "+ (marque) +" :");
            Double prixHT = sc.nextDouble();
            //apply overall reduce for 20k + car
            if (prixHT > 20000) {
                Reduc += 0.10;
            }
            switch (categorie) {
                // apply Reduc advantage of gold and plat member
                case "gold":Reduc = Reduc + 0.20;
                    if (elec == "oui"){
                        Reduc = Reduc + 0.10;
                    }
                    break;
                case "platinum" :Reduc =  Reduc + 0.15;
                    break;
                case "null":;
                    break;
                default:
                // invalid input
                    System.out.println("404 - La carte de fideliter est invalide");
                    isValid = true;
            }
            //get the final price
            double PrixTTC= (prixHT*(1+TVA)*Quantity);
            if (Reduc != 0.0){
                PrixTTC = PrixTTC*(1+Reduc);
            }
            double rReduc = Math.round(Reduc*100);
            double rPrixTTC =  Math.round(PrixTTC);
            System.out.println("Votre voiture coute (TTC):"+(rPrixTTC)+" (Felicitation vous avez une réduc de "+(rReduc)+"%)");


            System.out.println("Voulez-vous recommancer ? oui / non ");
            String reload = sc.next();
            if (reload == "oui") {
                isValid = false; // restart programme
                System.out.println("======================================================"); 

            }
            else {
                System.out.println("Merci, bonne journée");
                System.out.println("======================================================");
                sc.close();
                isValid = true; // stop the programme
            }
        }
    }
}