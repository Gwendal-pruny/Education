public class Etape1{

    String voyageur;
    String ingredients2;
    String ingredients3;
    float poids;
    float prix;
    
    public Etape1(String voyageur, String ingredients2, String ingredients3, float poids, float prix){
        this.voyageur = voyageur;
        this.ingredients2 = ingredients2;
        this.ingredients3 = ingredients3;
        this.poids = poids;
        this.prix = prix;
}


    public static void main(String args[]){
        Etape1 sandwich = new Etape1("salade", "tomate", "jambom", 100, 3);
        System.out.println("Voyageur : "+sandwich.voyageur+", "+sandwich.ingredients2+", "+sandwich.ingredients3+" | Poids : "+sandwich.poids+" | Prix : "+sandwich.prix+" $");
    }
}




// import java.util.Scanner;

// public class Etape1<Voyageur>{

//     String name;
//     int age;

    
//     public Etape1(String name, int age){
//         this.name = name;
//         this.age = age;
//     }


//     public Etape1(String args[]){
//         Etape1 voyageur = new Etape1("Hugo", 18);
//     }

//     public  Voyageur Etape(String[] args){
//         System.out.println(" | Nom : ");
//         name = sc.nextLine();
//         System.out.println(" | Age : ");
//         age = sc.nextInt();

//         Voyageur voyageur = new Voyageur(name, age);
//         return voyageur;
//     }

//     public static void main(String args[]){
//         System.out.println(Voyageur);
//         System.out.println(Constructor);
//         System.out.println(ConstructorDefault);

//     }

// }

