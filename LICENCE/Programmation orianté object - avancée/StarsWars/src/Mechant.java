public class Mechant {
    private String nom;
    private String prenom;
    private int anneeNaissance;
    private String nationalite;
    private String nomMaitre;
    private String prenomMaitre;
    private int anneeNaissanceMaitre;
    private String nationaliteMaitre;

    public Mechant(String nom, String prenom, int anneeNaissance, String nationalite, String nomMaitre, String prenomMaitre, int anneeNaissanceMaitre, String nationaliteMaitre) {
        this.nom = nom;
        this.prenom = prenom;
        this.anneeNaissance = anneeNaissance;
        this.nationalite = nationalite;
        this.nomMaitre = nomMaitre;
        this.prenomMaitre = prenomMaitre;
        this.anneeNaissanceMaitre = anneeNaissanceMaitre;
        this.nationaliteMaitre = nationaliteMaitre;
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

    public String getNomMaitre() {
        return nomMaitre;
    }

    public String getPrenomMaitre() {
        return prenomMaitre;
    }

    public int getAnneeNaissanceMaitre() {
        return anneeNaissanceMaitre;
    }

    public String getNationaliteMaitre() {
        return nationaliteMaitre;
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

    public void setNomMaitre(String nomMaitre) {
        this.nomMaitre = nomMaitre;
    }

    public void setPrenomMaitre(String prenomMaitre) {
        this.prenomMaitre = prenomMaitre;
    }
}



