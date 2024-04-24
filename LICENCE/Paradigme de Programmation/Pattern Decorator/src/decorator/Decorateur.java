package decorator;
abstract class Decorateur implements Boisson {
    protected Boisson boisson;

    public Decorateur(Boisson boisson) {
        this.boisson = boisson;
    }
}

