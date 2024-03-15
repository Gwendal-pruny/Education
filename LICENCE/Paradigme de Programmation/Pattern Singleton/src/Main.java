public class Main {
    public static void main(String[] args) {
        ArbreBinaire arbre = ArbreBinaire.creer();
        arbre.inserer(5);
        arbre.inserer(3);
        arbre.inserer(7);
        arbre.inserer(15);
        arbre.inserer(8);
        arbre.afficher();
        System.out.println("La taille de l'arbre est : " + arbre.taille());
        System.out.println("Est-ce que l'arbre contient la valeur 5 ? " + arbre.rechercher(5));
    }
}