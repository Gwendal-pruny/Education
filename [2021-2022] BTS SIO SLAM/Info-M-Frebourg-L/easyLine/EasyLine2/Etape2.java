import java.util;
public class Voyageur {
    private String nom;
    private int age;
    public Voyageur(String n, int age){
        Scanner sc=new Scanner(System.in);
        while(n.length()<2){
            System.out.println("ressaisir nom");
            n=sc.next();
        }
        this.nom=n;
        this.age=age;
    }
    public void afficher(){
        System.out.println(this.nom +" "+this.age);
    }
    public String getNom(){
        return this.nom+"waza";
    }
    public void setNom(String nom){
        Scanner sc=new Scanner(System.in);
        while(nom.length()<2){
            System.out.println("ressaisir nom");
            nom=sc.next();
        }
        this.nom=nom;

    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        System.out.println("nom O_o ?");
        String nom=sc.next();
       while(nom.length()<2){
            System.out.println("nom");
            nom=sc.next();
        }

        System.out.println("age?");
        int age=sc.nextInt();
        while(age<0){
            System.out.println("age?");
             age=sc.nextInt();
        }

        Voyageur monVoyageur = new Voyageur(nom,age);
        monVoyageur.afficher();

        Voyageur monVoyageur2 = new Voyageur();
        monVoyageur2.nom="erambert";
        monVoyageur2.age=18;
        monVoyageur2.afficher();

     } 

}
