package coffee;
public class CoffeeOrder {
    private final String type; // The type of coffee, e.g., Espresso, Latte.
    private final boolean milk; // Indicates if milk is added.
    private final boolean sugar; // Indicates if sugar is added.
    private final String extras; // Additional extras for the coffee, e.g., vanilla.

    public CoffeeOrder(String type, boolean milk, boolean sugar, String extras) {
        this.type = type;
        this.milk = milk;
        this.sugar = sugar;
        this.extras = extras == null ? "None" : extras; // Handle null extras.
    }

    @Override
    public String toString() {
        return "Coffee Order: Type=" + type + 
               ", Milk=" + (milk ? "Yes" : "No") + 
               ", Sugar=" + (sugar ? "Yes" : "No") + 
               ", Extras=" + extras;
    }
}
