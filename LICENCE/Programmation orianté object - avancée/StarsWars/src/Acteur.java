import java.util.ArrayList;
import java.util.Scanner;

public class Acteur {
    private String prenom;
    private String nom;
    private int annee;
    private String pseudonyme;
    private ArrayList<Personnage> personnages; // List to store the characters played by the actor

    // Constructor for Acteur class
    public Acteur(String nom, String prenom, int annee, String pseudonyme, ArrayList<Personnage> personnages) {
        this.annee = annee;
        this.prenom = prenom;
        this.nom = nom;
        this.pseudonyme = pseudonyme;
        this.personnages = personnages;
    }

    public void addPersonnage(Personnage personnage) {
        this.personnages.add(personnage);
    }

    // Constructor for Acteur class with only name
    public Acteur(String nom) {
        this.nom = nom;
        this.personnages = new ArrayList<>();
    }

    // Method to get the name of the actor
    public String getNom() {
        return this.nom;
    }

    // Method to get the characters played by the actor
    public ArrayList<Personnage> getPersonnages() {
        return this.personnages;
    }

    // Method to print the number of characters played by the actor
    public void nbPersonnages() {
        System.out.println(personnages.size());
    }

    // Overriding toString method to print Actor's name
    @Override
    public String toString() {
        return this.nom;
    }

    // Method to create a new Actor
    public static Acteur createActeur() {
        System.out.println("Création d'un acteur...\n");
        System.out.printf("Choissisez le côter obscure de la force : %s%n", "Sith");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Entrez le nom :");
        String nom = scanner.nextLine();

        System.out.println("Entrez le prénom :");
        String prenom = scanner.nextLine();

        System.out.println("Personnage joué :");
        String personnageInput = scanner.nextLine();
        ArrayList<Personnage> listePersonnage = new ArrayList<>();

        for (String pseudonyme : personnageInput.split(",") ) {
            listePersonnage.add(new Personnage(pseudonyme.trim()));
        };

        System.out.println("Entrez l'année de naissance :");
        int annee = Integer.parseInt(scanner.nextLine());

        Acteur acteur = new Acteur(nom, prenom, annee, nom, listePersonnage);
        return acteur;
    }
}