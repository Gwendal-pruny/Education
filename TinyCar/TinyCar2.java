//Question 1

class Padawan {
    public static void main(String[] args) {
        int prixTTC= 0;
        int prixHT= 0;
        double TVA= 0.1;
        int Quantity= 3;


        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :")
        string marque = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le model :")
        string model = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de la "+ (model)"de marque"+ (marque) " :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1*TVA)*Quantity);

        if (prixHT > 20 000 ) {
            System.out.println("Votre voiture coute (TTC):"(PrixTTC*0.10)+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}


//Question 2


class Padawan {
    public static void main(String[] args) {
        int prixTTC= 0;
        int prixHT= 0;
        int TVA= 0.20;
        int Quantity= 3;


        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :")
        string marque = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le model :")
        string model = sc.nextInt();
        System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ")
        string elec = sc.nextInt();
        if (elec == 'oui'){
            TVA = 5;
        }
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de la "+ (model)"de marque"+ (marque) " :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1+TVA)*Quantity);

        if (prixHT > 20 000 ) {
            System.out.println("Votre voiture coute (TTC):"(PrixTTC*0.10)+ " (Felicitation vous avez bonne conscience ! vive tesla  ou pas...!)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}


// Question 3

class Padawan {
    public static void main(String[] args) {
        int prixTTC= 0;
        int prixHT= 0;
        int TVA= 0.20;
        int Quantity= 3;
        string mdp;

        Scanner sc = new Scanner(System.in);
        System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
        string mdp = sc.nextInt();
        if (mdp != 42){
            System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
            stop;
        }
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :");
        string marque = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le model :");
        string model = sc.nextInt();
        System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
        string elec = sc.nextInt();
        if (elec == 'oui'){
            TVA = 5;
        }
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de la "+ (model)"de marque"+ (marque) " :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1+TVA)*Quantity);

        if (prixHT > 20 000 ) {
            System.out.println("Votre voiture coute (TTC):"(PrixTTC*0.10)+ " (Felicitation vous avez bonne conscience ! vive tesla  ou pas...!)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}

// Question 4

class Padawan {
    public static void main(String[] args) {

        // On initialise toutes les variables
        int prixTTC= 0;
        int prixHT= 0;
        int TVA= 0.20;
        int Quantity= 3;
        int Reduc= 0;
        string mdp;


        Scanner sc = new Scanner(System.in);
        //MDP
        System.out.println("Pour acceder a notre catalogue merci de repondre correctement => la réponse à la grande question sur la vie, l’univers et le reste :");
        string mdp = sc.nextInt();
        if (mdp != 42){
            System.out.println("Faux. Les inculte ne sont pas tolerer, chiao");
            stop; // stoper le programme
        }
        Scanner sc = new Scanner(System.in);
        // get carde info
        System.out.println("Veuillez indiquer si vous possèder une carte de fiddeliter : [oui/non]");
        string carte = sc.nextInt();
        // apply advantage for vip
        if (carte == 'oui'){
            System.out.println("Veuillez indiquer ca gamme : [gold/platinium]");
            string categorie = sc.nextInt();
        }
        else {
            categorie = nul;
        }
        Scanner sc = new Scanner(System.in);
        //get marque
        System.out.println("Veuillez saisir la marque :");
        string marque = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        //get model
        System.out.println("Veuillez saisir le model :");
        string model = sc.nextInt();
        //get v type
        System.out.println("Veuillez indiquer si le véhuicule est electique : [oui/non] ");
        string elec = sc.nextInt();
        // apply reduc if v type is electrique 
        if (elec == 'oui'){
            TVA = 5;
        }
        Scanner sc = new Scanner(System.in);
        // get v price
        System.out.println("Veuillez saisir le prix de la "+ (model)"de marque"+ (marque) " :");
        int prixHT = sc.nextInt();
        //get price without reduce adventages
        PrixTTC= (PrixHT*(1+TVA)*Quantity);
        switch (categorie) {
            // apply reduc adventage of gold and plat member
            case "gold":Reduc = Reduc + 0.20;
                if (elec == 'oui'){
                    Reduc = Reduc + 10
                }
                break;
            case "platinium" :Reduc =  Reduc + 15;
                break;
            case "nul":Reduc = Reduc;
                break;
            default:
            // invalide inpuit
                System.out.println("404 - La carte de fideliter est invalide");
                stop;
        }
        //apply overall reduce for 20k + car
        if (prixHT > 20 000 ) {
            Reduc = Reduc + 10;
        }
        //get the final price
        Prix = PrixTTC*(Reduc/100);
        System.out.println("Votre voiture coute (TTC):"+(Prix)" (Felicitation vous avez une réduc de "+Reduc "%");
}