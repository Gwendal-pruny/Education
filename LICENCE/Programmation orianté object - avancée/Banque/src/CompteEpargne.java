public class CompteEpargne implements CompteBancaire {
    private double solde;

    @Override
    public double consulterSolde() {
        return  solde;
    }

    @Override
    public void deposerArgent(double montant) {
        solde += montant;
    }

    @Override
    public void retirerArgent(double montant) throws SoldeInsuffisantException {
        if (montant > solde) {
            throw new SoldeInsuffisantException("Solde insuffisant pour le retrait.");
        }
        solde -= montant;
    }
    @Override
    public void supprimerCompte() {
        // Implementation of supprimerCompte
    }
}