import java.util.Scanner;

public class planting {
    
    public planting(String string) {
        
    }

    public static void main(String[] args) { 
        Scanner sc=new Scanner(System.in);
        System.out.println("Combien de fleurs souhaitez vous dans votre plantation ?");
        int numberOfFlowers = sc.nextInt();

        planting[] plantation = new planting[numberOfFlowers];
		plantation[0] = new plantings(); 
        

    }

}
