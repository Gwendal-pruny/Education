public class Gentil {
    private String nom;
    private String prenom;
    private int anneeNaissance;
    private String nationalite;

    public Gentil(String nom, String prenom, int anneeNaissance, String nationalite) {
        this.nom = nom;
        this.prenom = prenom;
        this.anneeNaissance = anneeNaissance;
        this.nationalite = nationalite;
    }

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public int getAnneeNaissance() {
        return anneeNaissance;
    }

    public String getNationalite() {
        return nationalite;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public void setAnneeNaissance(int anneeNaissance) {
        this.anneeNaissance = anneeNaissance;
    }

    public void setNationalite(String nationalite) {
        this.nationalite = nationalite;
    }

    @Override
    public String toString() {
        return "Acteur{" +
                "nom='" + nom + '\'' +
                ", prenom='" + prenom + '\'' +
                ", anneeNaissance=" + anneeNaissance +
                ", nationalite='" + nationalite + '\'' +
                '}';
    }
}
