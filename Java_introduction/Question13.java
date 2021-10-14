public class Question13 {
    public void affiche(){
        System.out.println(nom+" "+annee_naissance);
        }
    public void calcul_age(){
        int age=2011-annee_naissance;
        System.out.println("age = "+age);
    }
        --------------------------------------------------------------------------------------------------------
    public static void main(String args[]){
        Sandwich ingredients1=new ("dupont",1950);
        Personne ingredients2=new Personne("mercier",1962);
        Personne ingredients3=new Personne("mercier",1962);
        Personne prix=new Personne("mercier",1962);
        System.out.println(p1.nom);
        p1.affiche();
        p2.affiche();
        p3.calcul_age();
        p4.calcul_age();
    
}
