package coffee;
public class CoffeeOrderBuilder {
    private String type;
    private boolean milk = false; // Default no milk.
    private boolean sugar = false; // Default no sugar.
    private String extras;

    public CoffeeOrderBuilder setType(String type) {
        this.type = type;
        return this;
    }

    public CoffeeOrderBuilder setMilk(boolean milk) {
        this.milk = milk;
        return this;
    }

    public CoffeeOrderBuilder setSugar(boolean sugar) {
        this.sugar = sugar;
        return this;
    }

    public CoffeeOrderBuilder setExtras(String extras) {
        this.extras = extras;
        return this;
    }

    public CoffeeOrder build() {
        // Validate mandatory fields like type.
        if (type == null || type.trim().isEmpty()) {
            throw new IllegalStateException("Coffee type must be specified.");
        }
        return new CoffeeOrder(type, milk, sugar, extras);
    }
}
