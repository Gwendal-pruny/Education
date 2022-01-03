package TinyCar2;
import java.util.Scanner;

class Question3 {
    public static boolean isValid = false;
    

    public static void main(String[] args) {    
        Scanner sc = new Scanner(System.in);
    
        while(!isValid) {
            // On initialise toutes les variables
            double TVA= 0.20;
            int Quantity= 1;
            double Reduc = 0.0;
            String marque = "None";
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
            marque = sc.next();
            //get model
            System.out.println("Veuillez saisir le model :");
            String model = sc.next();
            //get v type
            System.out.println("Veuillez indiquer si le véhicule est electique : [oui/non] ");
            String elec = sc.next();
            // apply reduc if v type is electrique 
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
            //get the final price
            double PrixTTC= (prixHT*(1+TVA)*Quantity);
            if (Reduc != 0.0){
                PrixTTC = PrixTTC*(1+Reduc);
            }
            System.out.println("Votre voiture coute (TTC):"+(PrixTTC)+" (Felicitation vous avez une réduc de "+(Reduc*100)+"%)");


            System.out.println("Voulez-vous recommancer ? oui / non ");
            String reload = sc.next();
            if (reload != "non") {
                isValid = false; // recommancer le programme
            }
            else {
                System.out.println("Merci, bonne journée");
                sc.close();
                isValid = true; // stoper le programme
            }
        }
    }
}