package decorator;
class Cafe implements Boisson {
    @Override
    public String description() {
        return "Café";
    }

    @Override
    public double cout() {
        return 1.99;
    }
}

