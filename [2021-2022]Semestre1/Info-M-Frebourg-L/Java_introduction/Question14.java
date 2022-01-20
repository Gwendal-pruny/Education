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

