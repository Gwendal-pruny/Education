package TinyCar2;
import java.util.Scanner;

class Question3 {
    public static void main(String[] args) {
        
        // On initialise toutes les variables
        double TVA= 0.20;
        int Quantity= 3;
        int Reduc= 0;
        boolean isValid= false;
        String marque = "None";


        while(!isValid) {

            Scanner sc = new Scanner(System.in);
            //MDP
            System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
            int mdp = sc.nextInt();
            if (mdp != 42){
                System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
                sc.close();
                isValid = true; // stoper le programme
            }
            //get marque
            System.out.println("Veuillez saisir la marque :");
            while ( marque == "None" ){
                marque = sc.nextLine();
            }
            //get model
            System.out.println("Veuillez saisir le model :");
            String model = sc.nextLine();
            //get v type
            System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
            String elec = sc.nextLine();
            // apply reduc if v type is electrique 
            if (elec == "oui"){
                TVA = 0.05;
            }
            // get v price
            System.out.println("Veuillez saisir le prix de la "+ (model)+"de marque"+ (marque) +" :");
            int prixHT = sc.nextInt();
            //apply overall reduce for 20k + car
            if (prixHT > 20000) {
                Reduc = Reduc + 10;
            }
            //get the final price
            double PrixTTC= (prixHT*(1+TVA)*Quantity);
            double Prix = PrixTTC;
            if (Reduc != 0){
                Prix = PrixTTC*(Reduc/100);
            }
            System.out.println("Votre voiture coute (TTC):"+(Prix)+" (Felicitation vous avez une réduc de "+Reduc+"%)");


            System.out.println("Voulez-vous recommancer ? oui / non ");
            String reload = sc.nextLine();
            if (reload == "oui") {
                sc.close();
                isValid = false; // stoper le programme

            }
            else {
                System.out.println("Merci, bonne journée");
                sc.close();
                isValid = true; // stoper le programme

            }
        }
    }
}
