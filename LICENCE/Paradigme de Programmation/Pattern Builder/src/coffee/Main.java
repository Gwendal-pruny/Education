package coffee;
public class Main {
    public static void main(String[] args) {
        CoffeeOrderBuilder builder = new CoffeeOrderBuilder();
        CoffeeOrder espresso = builder.setType("Espresso").setMilk(false).setSugar(false).build();
        CoffeeOrder latte = builder.setType("Latte").setMilk(true).setSugar(true).setExtras("Vanilla").build();

        // Prints the description of espresso order
        System.out.println(espresso);
        // Prints the description of latte order with vanilla
        System.out.println(latte);
    }
}
