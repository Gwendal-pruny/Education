import java.util.Scanner;

public class Personnage {
    private String pseudonyme;
    private String prenom;
    private String nom;
    private String film_jouer;

    // Constructor for Personnage class
    public Personnage(String nom, String prenom, String film_jouer, String pseudonyme) {
        this.film_jouer = film_jouer;
        this.prenom = prenom;
        this.nom = nom;
        this.pseudonyme = pseudonyme;
    }


    // Constructor for Personnage class with only pseudonyme
    public Personnage(String pseudonyme) {
        this.pseudonyme = pseudonyme;
    }

    // Overriding toString method to print Personnage details
    @Override
    public String toString() {
        return  "Nom: " + nom +
                ", Prenom: " + prenom +
                ", Film joué: " + film_jouer +
                ", Pseudonyme: " + pseudonyme;
    }

    // Method to create a new Personnage
    public static Personnage createPersonnage() {
        System.out.println("Création d'un personnage...\n");
        System.out.printf("Choissisez le côter obscure de la force : %s%n", "Sith");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Entrez le pseudonyme :");
        String pseudonyme = scanner.nextLine();

        System.out.println("Entrez le nom :");
        String nom = scanner.nextLine();

        System.out.println("Entrez le prénom :");
        String prenom = scanner.nextLine();

        System.out.println("A jouer dans :");
        String film_jouer = scanner.nextLine();

        Personnage personnage = new Personnage(nom, prenom, film_jouer, pseudonyme);
        return personnage;
    }
}