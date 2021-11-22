import java.util.Scanner;

public class exo234 {
    public static void main(String[] args) {

        boolean isValid = true;
        int newcalc = 1;
        Scanner sc = new Scanner(System.in);


        while (isValid) {
            System.out.println("Merci de saisir la distance d'une planète par rapport aux soleil :");
            int newplanete = sc.nextInt();
            switch (newplanete) {
                case 60: System.out.println("La planète mercure ce trouve à M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");     
                    break;
                case 110 : System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 150 : System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;                
                case 230: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 800: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 1400: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 3000: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 4400: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
                case 4800: System.out.println("La planète mercure ce trouve à x M de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                    break;
            }

            while (newcalc != 0) {
                System.out.println("Nouveaux calcule ? oui / non ");
                String reload = sc.nextLine();
                if (reload == "non") {
                    newcalc = 1;
                }
                else {
                    System.out.println("Merci de saisir la distance d'une planète par rapport aux soleil :");   
                }
            }
    
    }
}}