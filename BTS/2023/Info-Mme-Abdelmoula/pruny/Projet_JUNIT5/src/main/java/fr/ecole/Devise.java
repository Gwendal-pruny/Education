package fr.ecole;

public class Devise {
    private int quantite;
    private String monnaie;

    public Devise(int somme, String monnaie) {
        this.quantite = somme;
        this.monnaie = monnaie;
    }
    public int getQuantite() {
        return quantite;
    }
    public String getMonnaie() {
        return monnaie;
    }
    public Devise add(Devise m) {
        return new Devise(getQuantite()+m.getQuantite(), getMonnaie());
    }

    @Override
    public boolean equals(Object obj) {
        // On s'assure qu'obj est une Devise
        if(!(obj instanceof Devise)) {
            System.out.println("l'objet comparé n'est pas une DEVISE");
            return false;
        }
        // On s'assure que l'Objet n'est pas null
        if(obj == null) return false;
        //Comparer les deux objets this et obj
        // conversion explicite d'OBJ de Object à Devise
        Devise objDevise= (Devise)obj;
        if(this.getMonnaie().equals(objDevise.getMonnaie())){
            //Comparer ma somme
            if(this.getQuantite()== objDevise.getQuantite()) return true;
        }
        return false;
    }
}
