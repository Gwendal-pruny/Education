//Question 1
//Pas comprit 

//age=20; i=0 ; i=1+1 ; // int
//j=i ; //char 
//voiture= "peugeot" ;  //string
//h=k+k ; // char
//majeur=(age>18) // bool

//Question 2

// déjà fait 


//Question 3

class Padawan {
    public static void main(String[] args) {
        int prixTTC= 0;
        int prixHT= 0;
        double TVA= 0.1;
        int Quantity= 3;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de votre article :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1*TVA)*Quantity);

        if (prixHT > 100 ) {
            System.out.println((PrixTTC*0.10)+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}


//Question 4

class Padawan {
    public static void main(String[] args) {
        int prixTTC= 0;
        int prixHT= 0;
        double TVA= 0.1;
        int Quantity= 3;


        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir la marque :");
        string marque = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le model :");
        string model = sc.nextInt();
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le prix de la "+ (model)"de marque"+ (marque) " :");
        int prixHT = sc.nextInt();
        PrixTTC= (PrixHT*(1+TVA)*Quantity);

        if (prixHT > 100 ) {
            System.out.println("Votre voiture coute (TTC):"(PrixTTC*0.10)+ " (Felicitation vous avez une remise de 10%)");
        } else {
            System.out.println(Prix TTC);
        }
    }
}
