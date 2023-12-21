import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
import java.util.Comparator;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;

public class Film {
    private String titre;
    private String realisateur;
    private int annee;
    private String genre;
    private ArrayList<Acteur> listeActeurs;
    private int cout;
    private int recette;

    // Constructor for Film class
    public Film(String titre, String realisateur, int annee, String genre, int cout, int recette) {
        this.titre = titre;
        this.realisateur = realisateur;
        this.annee = annee;
        this.genre = genre;
        this.cout = cout;
        this.recette = recette;
        this.listeActeurs = new ArrayList<>();
    }

    // Overriding toString method to print Film details
    @Override
    public String toString() {
        StringBuilder liste = new StringBuilder();
        for (Acteur acteur : listeActeurs) {
            if (liste.length() > 0) {
                liste.append(", ");
            }
            liste.append(acteur.getNom());
        }
        return  "Titre: " + titre +
                ", Realisateur: " + realisateur +
                ", Annee: " + annee +
                ", Genre: " + genre +
                ", Acteurs: " + liste +
                ", Cout: " + cout +
                ", Recette: " + recette;
    }

    // Method to create a new Film
    public static Film createFilm() {
        System.out.println("Création d'un film...\n");
        Scanner scanner = new Scanner(System.in);

        System.out.println("Entrez le nom du film :");
        String titre = scanner.nextLine();

        System.out.println("Entrez le nom du réalisateur :");
        String realisateur = scanner.nextLine();

        System.out.println("Entrez l'année de sortie :");
        int annee = Integer.parseInt(scanner.nextLine());

        System.out.println("Entrez le genre :");
        String genre = scanner.nextLine();

        System.out.println("Entrez le cout :");
        int cout = scanner.nextInt();

        System.out.println("Entrez la recette :");
        int recette = scanner.nextInt();

        Film film = new Film(titre, realisateur, annee, genre, cout, recette);

        System.out.println("Entrez le nom des acteurs (séparés par des virgules) :");
        scanner.nextLine(); // Consume newline left-over
        String acteursInput = scanner.nextLine();
        for (String nom : acteursInput.split(",") ) {
            film.listeActeurs.add(new Acteur(nom.trim()));
        };

        System.out.println("Le film à été créé avec succès :\n");
        return film;
    }

    // Method to print actors of the film
    public void printActeurs() {
        System.out.println("Acteurs du film : " + listeActeurs);
    }

    // Method to print number of actors in the film
    public void nbActeurs() {
        System.out.println("Nombres d'acteurs dans le film : " + listeActeurs.size());
    }

    // Method to calculate and print the profit of the film
    public void calculBenefice() {
        int benefice = recette - cout;
        boolean boolbenefice = benefice > 0;
        System.out.println("Caulcule bénéfice : " + benefice);
        System.out.println("Bénéfice : Positif | Négatif -> " + boolbenefice);

    }

    // Method to check if the film was released before a certain year
    public void isBefore(int annee) {
        System.out.println(this.annee < annee);
    }

    // Method to print the number of characters in the film
    public void nbPersonnages() {
        int total = 0;
        for (Acteur acteur : listeActeurs) {
            total += acteur.getPersonnages().size();
        }
        System.out.println(total);
    }

    // Method to sort actors in alphabetical order
    public void tri() {
        Collections.sort(this.listeActeurs, Comparator.comparing(Acteur::getNom));
    }

    // Method to create a backup of films
    public static void makeBackUp(Map<Integer, Film> films) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("backup.txt"))) {
            for (Map.Entry<Integer, Film> entry : films.entrySet()) {
                Film film = entry.getValue();
                String line = entry.getKey() + " - " + film.titre + " - " + (film.recette - film.cout);
                writer.write(line);
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }
    public void setListeActeurs(ArrayList<Acteur> listeActeurs) {
        this.listeActeurs = listeActeurs;
    }
}