package Arbre;

/**
 * Main class to demonstrate operations on the binary tree.
 */
public class Main {
    public static void main(String[] args) {
        // Creating an instance of a binary tree using the singleton empty tree.
        ArbreBinaire arbre = ArbreBinaire.creer();
        arbre.inserer(5);
        arbre.inserer(3);
        arbre.inserer(7);
        arbre.inserer(15);
        arbre.inserer(8);

        // Displaying the tree and checking some functionalities.
        arbre.afficher();
        System.out.println("La taille de l'arbre est : " + arbre.taille());
        System.out.println("Est-ce que l'arbre contient la valeur 5 ? " + arbre.rechercher(5));
    }
}
