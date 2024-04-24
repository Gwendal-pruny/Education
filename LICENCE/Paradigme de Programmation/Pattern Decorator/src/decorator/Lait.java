package decorator;
class Lait extends Decorateur {
    public Lait(Boisson boisson) {
        super(boisson);
    }

    @Override
    public String description() {
        return boisson.description() + ", avec lait";
    }

    @Override
    public double cout() {
        return boisson.cout() + 0.50;
    }
}

