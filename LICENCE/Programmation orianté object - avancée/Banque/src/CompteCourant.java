public class CompteCourant implements CompteBancaire {
    private double solde;

    // Constructeur, getters, setters

    @Override
    public double consulterSolde() {
        return solde;
    }

    @Override
    public void deposerArgent(double montant) {
        solde += montant;
        System.out.println(montant + " ajouté au compte courant.");
    }

    @Override
    public void retirerArgent(double montant) throws SoldeInsuffisantException {
        if (solde < montant) {
            throw new SoldeInsuffisantException("Solde insuffisant pour le retrait.");
        }
        solde -= montant;
        System.out.println(montant + " retiré du compte courant.");
    }
    @Override
    public void supprimerCompte() {
        // Implementation of supprimerCompte
    }
}
