import java.util.ArrayList;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // Create a collection to store films
        ArrayList<Film> collection = new ArrayList<>();
        // Create a map to store films with their release year as the key
        HashMap<Integer, Film> films = new HashMap<>();
        // Create a scanner to read user input
        Scanner scanner = new Scanner(System.in);

        // Start a loop to display the menu until the user chooses to quit
        while (true) {
            try {
                // Display the menu
                System.out.println("\n=========== Menu =============");
                System.out.println("1. Créer un film");
                System.out.println("2. Créer un acteur");
                System.out.println("3. Créer un personnage");
                System.out.println("4. Afficher la collection de films");
                System.out.println("5. Trier les acteurs par ordre alphabétique");
                System.out.println("6. Créer une sauvegarde");
                System.out.println("7. Quitter");
                System.out.print("Choisissez une option : ");

                // Read the user's choice
                int option = scanner.nextInt();

                // Perform the appropriate action based on the user's choice
                switch (option) {
                    case 1:
                        // Create a new film and add it to the collection
                        Film film = Film.createFilm();
                        collection.add(film);
                        break;
                    case 2:
                        // Create a new actor
                        Acteur acteur = Acteur.createActeur();
                        System.out.println("\nL'acteur a été créé avec succès :\n" + acteur);
                        break;
                    case 3:
                        // Create a new character
                        Personnage personnage = Personnage.createPersonnage();
                        System.out.println("\nLe personnage a été créé avec succès :\n" + personnage);
                        break;
                    case 4:
                        // Display the film collection
                        System.out.println("\n=========== Collection de films =============");
                        for (Film film1 : collection) {
                            System.out.println(film1);
                            System.out.println("=========== Acteurs =============");
                            film1.printActeurs(); // Print the actors of the film
                            film1.nbActeurs(); // Print the number of actors in the film
                            film1.calculBenefice(); // Print the profit of the film
                            film1.isBefore(2023); // Print whether the film was released before 2000
                            film1.nbPersonnages(); // Print the number of characters in the film
                            System.out.println("=========== Personnages =============");
                        }
                        break;
                    case 5:
                        // Sort the actors in alphabetical order
                        for (Film film1 : collection) {
                            film1.tri();
                        }
                        System.out.println("Les acteurs ont été triés par ordre alphabétique.");
                        break;
                    case 6:
                        // Create a backup of the films
                        Film.makeBackUp(films);
                        System.out.println("Une sauvegarde a été créée.");
                        break;
                    case 7:
                        // Quit the program
                        System.out.println("Au revoir !");
                        return;
                    default:
                        // Handle invalid options
                        System.out.println("Option non reconnue. Veuillez choisir une option valide.");
                }
            } catch (InputMismatchException e) {
                // Handle input errors
                System.out.println("Erreur de frappe. Veuillez entrer un nombre.");
                scanner.next(); // Clear the invalid input
            }
        }
    }
}