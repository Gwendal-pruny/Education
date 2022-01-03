import java.util.Scanner;

public class Etape1<Voyageur>{

    String name;
    int age;

    
    public Etape1(String name, int age){
        this.name = name;
        this.age = age;
    }


    public Etape1(String args[]){
        Etape1 voyageur = new Etape1("Hugo", 18);
    }

    public  Voyageur Etape(String[] args){
        System.out.println(" | Nom : ");
        name = sc.nextLine();
        System.out.println(" | Age : ");
        age = sc.nextInt();

        Voyageur voyageur = new Voyageur(name, age);
        return voyageur;
    }

    public static void main(String args[]){
        System.out.println(Voyageur);
        System.out.println(Constructor);
        System.out.println(ConstructorDefault);

    }

}

