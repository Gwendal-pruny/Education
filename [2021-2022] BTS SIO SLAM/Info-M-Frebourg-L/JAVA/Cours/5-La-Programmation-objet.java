// Modifier le programme précédent pour qu’il puisse créer deux autres objets p3 et p4.
// Réaliser une classe Sandwich qui possède comme propriété trois ingrédients, un poids et un prix.

public class Question13{

    String ingredients1;
    String ingredients2;
    String ingredients3;
    float poids;
    float prix;
    
    public Question13(String ingredients1, String ingredients2, String ingredients3, float poids, float prix){
        this.ingredients1 = ingredients1;
        this.ingredients2 = ingredients2;
        this.ingredients3 = ingredients3;
        this.poids = poids;
        this.prix = prix;
}


    public static void main(String args[]){
        Question13 sandwich = new Question13("salade", "tomate", "jambom", 100, 3);
        System.out.println("Ingredients : "+sandwich.ingredients1+", "+sandwich.ingredients2+", "+sandwich.ingredients3+" | Poids : "+sandwich.poids+" | Prix : "+sandwich.prix+" $");
    }
}

// Créer un objet correspondant à la classe Sandwich en utilisant le constructeur .
// Réaliser une classe logement qui possède un nombre de pièce, une surface, une adresse, un prix.
// Créer deux objets correspondant à la classe.

public class Question13{

  String adresses;
  String ingredients2;
  String ingredients3;
  String ingredients4;
  float poids;
  float prix;
  
  public Question13(String ingredients1, String ingredients2, String ingredients3, float poids, float prix){
      this.ingredients1 = ingredients1;
      this.ingredients2 = ingredients2;
      this.ingredients3 = ingredients3;
      this.poids = poids;
      this.prix = prix;
  }


  public static void main(String args[]){
      Question13 sandwich = new Question13("salade", "tomate", "jambom", 100, 3);
      System.out.println("Ingredients : "+sandwich.ingredients1+", "+sandwich.ingredients2+", "+sandwich.ingredients3+" | Poids : "+sandwich.poids+" | Prix : "+sandwich.prix+" $");
  }
}

// Réaliser une classe Etudiant qui possède un nom, un prénom, un numéro, une date de naissance et une adresse. Ces éléments sont protégés.
// On réalisera les accesseurs et les modificateurs nécessaires.
// Créer 3 étudiants et modifier le nom du premier, afficher la date de naissance du deuxième, modifier le numéro du troisième tout en affichant son nom.


// Créer une classe Propriétaire. Cette classe possède comme propriété un nom, et un logement.
// Créer deux objets correspondant à la classe.
// Le premier achète un logement t1. Il le vend au propriétaire p2.
// Ecrire le code correspondant.

