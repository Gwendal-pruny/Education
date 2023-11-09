import java.util.Scanner;
class evaluation {
    public static void main(String[] args) {
        
        // On initialise toutes les variables des accessoire
        Scanner sc = new Scanner(System.in);

        String[] cargo = {"Cargaison 1", "Cargaison 2", "Cargaison 3", "Cargaison 4", "Cargaison 5", "Cargaison 6", "Cargaison 7", "Cargaison 8", "Cargaison 9", "Cargaison 10"};
        int[] tonnage = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int NumberOfCargoRep = 0;

        System.out.print("\033[H\033[2J");
        System.out.println("Bienvenue sur l'application de transport de fret, merci de suivre les indication !");
        System.out.print(" ");

        for(int i=0; i<10 ; i++) {
            for(int NumberOfCargo = 0; NumberOfCargoRep > NumberOfCargo; NumberOfCargo++) {
                System.out.println("Cargaison :"+cargo[NumberOfCargo] + "  ------->  " + tonnage[NumberOfCargo]+ " Tonnes");

            }
            //////////////////////////////////////////////////////////////// TYPE //////////////////////////////////////////////////////////////////
            System.out.println("Type de cargaison :");
            String UserCargoType = sc.next();
            cargo[i] = UserCargoType;
            //////////////////////////////////////////////////////////////// TONNAGE //////////////////////////////////////////////////////////////////
            System.out.println("Poid de votre cargaison :");
            int UserCargoTon = sc.nextInt();
            tonnage[i] = UserCargoTon;


            NumberOfCargoRep = NumberOfCargoRep + 1;
            System.out.println("Souhaitez-vous rajouter une autre cargaison ["+NumberOfCargoRep+"/10] ? [oui/non]");
            String Choice = sc.next();
            if("non".equals(Choice)) {
                System.out.println("Résuletat de vos atributions :");
                for(int NumberOfCargo = 0; NumberOfCargoRep > NumberOfCargo; NumberOfCargo++) {
                    System.out.println("Cargaison :"+cargo[NumberOfCargo] + "  ------->  " + tonnage[NumberOfCargo]+ " Tonnes");
                }
                int maxNum = tonnage[0];
                for (int o : tonnage) {
                    if (o > maxNum)
                        maxNum = o;
                }
                int somme = 0, moy;
                System.out.println("Poids le plus lourd :" + maxNum);
                for(int m = 0; m < tonnage.length; m++)
                    somme += tonnage[m];
                    moy = somme / tonnage.length; 
                System.out.println("La moyenne est: " + moy);
                i = 11;
            }
        }
    }
}

