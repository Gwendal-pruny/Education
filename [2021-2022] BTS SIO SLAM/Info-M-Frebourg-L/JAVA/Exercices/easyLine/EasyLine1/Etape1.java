import java.util.Scanner;
class Voyageur  {
    public String nom;
    public int age;
    public Voyageur(String n, int a) {
        this.nom = n;
        this.age = a;
    }
}

public Voyageur(){

}
public void affiche(){
    System.out.println(nom+" "+age);
}

public void calcul_age(){
    int age=2021-age;
    System.out.println("age = "+age);
}

public String tostring(){
    return "le nom de voyage est"+this.nom+" l'age de voygeur est "+this.age;
}
public static void main(String args[]){
    Voyageur p1=new Voyageur("Jack",2000);
    Voyageur p2=new Voyageur("Arncess",2001);
    System.out.println(p1.nom);
    p1.affiche();
    p2.affiche();
    p1.calcul_age();
    p2.calcul_age();
}