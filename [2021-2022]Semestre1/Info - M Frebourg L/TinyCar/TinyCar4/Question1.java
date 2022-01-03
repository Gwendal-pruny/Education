package TinyCar4;

import java.util.Scanner;

class Question1 {
    public static void main(String[] args) {
        
        // On initialise toutes les variables
        double TVA= 1.20;
        int Quantity= 3;
        double Reduc= 0;
        String categorie;
        String carte = "none";
        int mdp;
        // On initialise toutes les variables des accessoire

        String[] acces = {"Engeliver", "Tapis conducteur", "batterie", "Hawaiien", "Ethylotest(x8)"};
        double[] accesprix = {35, 12, 70, 4, 5};

        Scanner sc = new Scanner(System.in);
        //MDP
        System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
        mdp = sc.nextInt();
        if (mdp != 42){
            System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
            sc.close();
        }
        System.out.println("Souhaitez-vous acheter des accessoire ou une voiture ? [voiture/accessoire]");
        String choice = sc.next();
        if (choice.equals("voiture")){
            // get carde info
            System.out.println("Veuillez indiquer si vous possèder une carte de fiddeliter : [oui/non]");
            carte = sc.next();
            // apply advantage for vip
            if ("oui".equals(carte)){
                categorie = null;
                System.out.println("Veuillez indiquer ca gamme : [gold/platinium]");
                categorie = sc.next();
            }
            else {
                System.out.println("Veuillez indiquer ca gamme : [gold/platinium]");
                categorie = sc.next();
            }
            //get marque
            System.out.println("Veuillez saisir la marque :");
            String marque = sc.next();
            //get model
            System.out.println("Veuillez saisir le model :");
            String model = sc.next();
            //get v type
            System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
            String elec = sc.next();
            // apply reduc if v type is electrique 
            if ("oui".equals(elec)){
                TVA = 5;
            }
            // get v price
            System.out.println("Veuillez saisir le prix de la "+ (model)+"de marque"+ (marque)+ " :");
            int prixHT = sc.nextInt();
            //get price without reduce adventages
            double PrixTTC = (prixHT*TVA)*Quantity;
            switch (categorie) {
                // apply reduc adventage of gold and plat member
                case "gold":Reduc = Reduc + 0.20;
                    if (elec == "oui"){
                        Reduc = Reduc + 0.10;
                    }
                    break;
                case "platinium" :Reduc =  Reduc + 0.15;
                    break;
                case "nul":;
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
            System.out.println("Votre voiture coute (TTC):"+(prix)+" (Felicitation vous avez une réduc de "+Reduc*10 +"% avec une TVA à"+TVA*10+"%)");
            sc.close();
        }
        else if (choice.equals("accessoire")){
            for(int i=0; i<5 ; i++) {
                System.out.println(acces[i] + "  ------->  " + accesprix[i]);
            }
    }
}}

