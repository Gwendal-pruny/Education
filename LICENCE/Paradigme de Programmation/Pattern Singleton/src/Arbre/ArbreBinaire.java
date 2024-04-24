package Arbre;

/**
 * This class represents a binary tree with Singleton pattern for an empty tree.
 * It includes methods to insert values, check tree size, search values, and display tree contents.
 */
public class ArbreBinaire {
    private Integer clef;
    private ArbreBinaire gauche;
    private ArbreBinaire droit;
    private static final ArbreBinaire arbreVide = new ArbreBinaire();

    /**
     * Private constructor for creating empty tree nodes.
     */
    private ArbreBinaire() {
        this.clef = null;
        this.gauche = null;
        this.droit = null;
    }

    public Integer getClef() {
        return clef;
    }

    public void setClef(Integer clef) {
        this.clef = clef;
    }

    public ArbreBinaire getGauche() {
        return gauche;
    }

    public void setGauche(ArbreBinaire gauche) {
        this.gauche = gauche;
    }

    public ArbreBinaire getDroit() {
        return droit;
    }

    public void setDroit(ArbreBinaire droit) {
        this.droit = droit;
    }

    /**
     * Returns the singleton instance of the empty tree.
     */
    public static ArbreBinaire creer() {
        return arbreVide;
    }

    /**
     * Checks if the current node is empty.
     */
    public boolean estVide() {
        return this == arbreVide;
    }

    /**
     * Calculates and returns the size of the tree.
     */
    public int taille() {
        if (estVide()) {
            return 0;
        } else {
            int tailleGauche = (gauche != null) ? gauche.taille() : 0;
            int tailleDroit = (droit != null) ? droit.taille() : 0;
            return 1 + tailleGauche + tailleDroit;
        }
    }

    /**
     * Searches for a given value in the tree.
     */
    public boolean rechercher(Integer valeur) {
        if (estVide()) {
            return false;
        } else if (this.clef.equals(valeur)) {
            return true;
        } else {
            boolean trouveGauche = (gauche != null) && gauche.rechercher(valeur);
            boolean trouveDroit = (droit != null) && droit.rechercher(valeur);
            return trouveGauche || trouveDroit;
        }
    }

    /**
     * Inserts a value into the binary tree at the appropriate position.
     */
    public void inserer(Integer valeur) {
        if (estVide()) {
            this.clef = valeur;
            this.gauche = new ArbreBinaire();
            this.droit = new ArbreBinaire();
        } else if (valeur < this.clef) {
            if (gauche != null) gauche.inserer(valeur);
        } else if (valeur > this.clef) {
            if (droit != null) droit.inserer(valeur);
        }
    }

    /**
     * Displays the contents of the tree in in-order traversal.
     */
    public void afficher() {
        if (!estVide()) {
            if (gauche != null) gauche.afficher();
            System.out.println(this.clef);
            if (droit != null) droit.afficher();
        }
    }
}
