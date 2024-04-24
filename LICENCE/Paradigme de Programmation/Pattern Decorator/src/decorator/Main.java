package decorator;

public class Main {
    public static void main(String[] args) {
        Boisson cafe = new Cafe();
        cafe = new Lait(cafe);
        cafe = new Sucre(cafe);
        cafe = new Caramel(cafe);

        System.out.println(cafe.description() + " coûte " + String.format("%.2f", cafe.cout()) + " euros.");
    }
}
