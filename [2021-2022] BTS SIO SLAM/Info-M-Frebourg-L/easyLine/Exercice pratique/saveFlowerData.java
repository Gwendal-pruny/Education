import java.util.Scanner;

// ! COULEUR 1
// ! COULEUR 2
// ! TAILLE
// ! NOM

public class saveFlowerData {
    public String primaryColor;
    public String secondaryColor;
    public int height;
    public String name;



    public saveFlowerData() {            
        Scanner sc=new Scanner(System.in);

        System.out.println("? Primary color: ");
        primaryColor=sc.nextLine();
        while(primaryColor.length()<2){
            System.out.println("? Primary color: ");
            primaryColor=sc.nextLine();
        }

        System.out.println("? Secondary color: ");
        secondaryColor=sc.nextLine();
        while(secondaryColor.length()<2){
            System.out.println("? Secondary color: ");
            secondaryColor=sc.nextLine();
        }

        System.out.println("? height : ");
        height=sc.nextInt();
        while(height<1){
            System.out.println("? height : ");
            height=sc.nextInt();
        }

        System.out.println("? Name : ");
        name=sc.next();
        while(name.length()<2){
            System.out.println("? Name : ");
            name=sc.next();
        }

     }

    
    private void parramettersModification() {
        Scanner sc=new Scanner(System.in);
        System.out.println("? height : ");
        height=sc.nextInt();
    }
    
    private static void newFlower() {
        Scanner sc1=new Scanner(System.in);
        saveFlowerData newFlowerData = new saveFlowerData();
        newFlowerData.toString();

        System.out.println("\nSouhaitez-vous modifier la propriété 'taille' de la fleur ? (0 = oui /1 = non): ");
        int YesOrNo=sc1.nextInt();
        while(YesOrNo == 0){
            newFlowerData.parramettersModification();
            System.out.println("\nSouhaitez-vous continuer de modifier la propriété 'taille' de la fleur ? (oui / non): ");
            YesOrNo=sc1.nextInt();
        }

        System.out.println("\nNouvelle fleurs ajouter a la plantation");
        newFlowerData.toString();
        planting[] flower = new planting[10]; 
		flower[0] = new planting(newFlowerData.toString());
    }


    @Override
    public String toString() {
        return "\nCouleur principale : "+primaryColor+"\n Couleur secondaire : "+this.secondaryColor+"\n Hauteur : "+this.height+"\n Nom : "+this.name+" ";
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        System.out.println("\nSouhaitez-vous allez a votre plantation ( oui ) \n ou rajoutez une fleurs a votre plantation ? ( non ): ");
        String YesOrNo=sc.nextLine();
        while(YesOrNo != "oui"){
            System.out.println("En cours d'ajout d'une nouvelle fleurs a la plantaiton ! ");
            newFlower();
            System.out.println("\nSouhaitez-vous allez a votre plantation ( oui ) \n ou rajoutez une fleurs a votre plantation ? ( non ):");
            YesOrNo=sc.nextLine();


        }
    }
}




