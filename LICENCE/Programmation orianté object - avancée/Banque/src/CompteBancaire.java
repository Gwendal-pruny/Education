public interface CompteBancaire {
    void deposerArgent(double montant);
    void retirerArgent(double montant) throws SoldeInsuffisantException;
    void supprimerCompte();

    double consulterSolde();
}
