import java.util.Scanner;
public class Voyageur {
    private String nom;
    private int age;
    public Voyageur(){
    }

    public Voyageur (String n, int age){
        Scanner sc=new Scanner(System.in);
        while(n.length()<2){
            System.out.println("ressaisir nom");
            n=sc.next();
        }

        while(age<0){
            System.out.println("ressaisir votre age2");
            age=sc.nextInt();


        }
       this.nom=n;
        this.age=age;

    }
    public void setNom(String nom){

        Scanner sc=new Scanner(System.in);
        while(nom.length()<2){
            System.out.println("ressaisir nom");
            nom=sc.next();
        }
        this.nom=nom;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int ageV) {
        Scanner sc=new Scanner(System.in);
        while(ageV<0){
          System.out.println("ressaisir un age");
          ageV=sc.nextInt();
        } 
        this.age=ageV;
    }
public void afficher(){
        System.out.println(this.nom + " "+this.age);
     }
    public String getNom(){
            return this.nom;
    }

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Veuillez saisir votre age :");
        int age = sc.nextInt();
        /while(age<0) {
            System.out.println("Votre nombre entré est négatif, veuillez rentrez un âge positif :");
            age = sc.nextInt();

        }


        System.out.println("Veuillez sasir votre nom :");
        String nom = sc.next();
        System.out.println(nom.length()<2);
        while(nom.length()<2) {
            System.out.println("Votre nom doit être composé d'au moins deux caractères, veuillez recommencer :");
            nom= sc.next();
        }
        if (age<1){
            System.out.println("Vous êtes un nourisson");
        }
        else if (age<18 && age>1){
            System.out.println("Vous êtes un enfant");
        }
        else if (age<60 && age>18){
            System.out.println("Vous êtes un adulte");
        }
        else if (age>60);
            System.out.println("Vous êtes un senior");
        }
        Voyageur monVoyageur = new Voyageur(nom,age);
        monVoyageur.afficher();

        nom="Josué";
        age=18;
        Voyageur monVoyageur2 = new Voyageur(nom,age);
        monVoyageur2.afficher();

         }
    }