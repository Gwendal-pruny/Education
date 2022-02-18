import java.util.Scanner;
class Question4 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir le premier nombre :");
        int a = sc.nextInt();
        System.out.println("Veuillez saisir le second nombre :");
        int b = sc.nextInt();
        System.out.println("Vous avez saisi : "+(a + b));
    }
}