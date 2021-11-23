import java.util.Scanner;

class exo23456 {
    public static void main(String[] args) {
        boolean restart = true;
        int laboucle = 0;
        Scanner sc = new Scanner(System.in);

        while (laboucle == 0) {
            System.out.println("Merci de saisir la distance d'une planète par rapport aux soleil :");
            int newplanete = sc.nextInt();
            switch (newplanete) {
                case 60: System.out.println("La planète mercure ce trouve à 60 Milliard Km aux minimum du soleil et en moyenne à X milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");     
                    break;
                case 110 : System.out.println("La planète mercure ce trouve à 110 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 150 : System.out.println("La planète mercure ce trouve à 150 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;                
                case 230: System.out.println("La planète mercure ce trouve à 230 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 800: System.out.println("La planète mercure ce trouve à 800 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 1400: System.out.println("La planète mercure ce trouve à 1400 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 3000: System.out.println("La planète mercure ce trouve à 3000 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 4400: System.out.println("La planète mercure ce trouve à 4400 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
                case 4800: System.out.println("La planète mercure ce trouve à 4800 Milliard de Km aux minimum du soleil et en moyenne à x milliard de killomètre du soleil");
                        System.out.println("Le rapport temps / distance entre la terre et le soleil est de"+(CALCRAPPORT)+"");
                        System.out.println("Le temps nécéssaire de la planette la plus proche au soleil est de"+(CALCTEMPS)+" X");
                    break;
            }

            System.out.println("Voulez-vous recommancer ? [(oui) 1 / 0 (non)] ");
            int choice = sc.nextInt();
            if (choice == 0) {
                laboucle = 1;
            }

        }

            // Scanner sc1 = new Scanner(System.in);
            // System.out.println("Nouveaux calcule ? oui / non ");
            // String reload = sc1.nextLine();
            // if (reload == "non") {
            //     laboucle = 1;
            // }
    
    }
}