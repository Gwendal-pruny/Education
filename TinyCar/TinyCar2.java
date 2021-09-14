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

        Scanner sc = new Scanner(System.in);
        System.out.println("Pour acceder a notre catalogue merci de repondre correctement => Quelle est la réponse a l'univers ? :");
        string mdp = sc.nextInt();
        if (mdp !=){
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