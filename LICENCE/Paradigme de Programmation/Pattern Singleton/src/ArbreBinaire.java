public class ArbreBinaire {
    private Integer clef;
    private ArbreBinaire gauche;
    private ArbreBinaire droit;
    private static ArbreBinaire arbreVide = new ArbreBinaire();

    public ArbreBinaire() {
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

    public static ArbreBinaire creer() {
        return new ArbreBinaire();
    }

    public boolean estVide() {
        return this == arbreVide;
    }

    public int taille() {
        int tailleGauche = 0;
        int tailleDroit = 0;
    
        if (this.clef == null) {
            return 0;
        } else {
            if (this.gauche != null) {
                tailleGauche = this.gauche.taille();
            }
            if (this.droit != null) {
                tailleDroit = this.droit.taille();
            }
            return 1 + tailleGauche + tailleDroit;
        }
    }

    public boolean rechercher(Integer valeur) {
        if (this.clef == null) {
            return false;
        } else if (this.clef.equals(valeur)) {
            return true;
        } else {
            boolean trouveGauche = false;
            boolean trouveDroit = false;
            if (this.gauche != null) {
                trouveGauche = this.gauche.rechercher(valeur);
            }
            if (!trouveGauche && this.droit != null) {
                trouveDroit = this.droit.rechercher(valeur);
            }
            return trouveGauche || trouveDroit;
        }
    }

    public void inserer(Integer valeur) {
        if (this.clef == null) {
            this.clef = valeur;
            this.gauche = ArbreBinaire.creer();
            this.droit = ArbreBinaire.creer();
        } else if (valeur < this.clef) {
            this.gauche.inserer(valeur);
        } else if (valeur > this.clef) {
            this.droit.inserer(valeur);
        }
    }

    public void afficher() {
        if (this.clef != null) {
            if (this.gauche != null) {
                this.gauche.afficher();
            }
            System.out.println(this.clef);
            if (this.droit != null) {
                this.droit.afficher();
            }
        }
    }
}