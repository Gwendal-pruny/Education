public interface ClientBanque {
    void setId(int id);
    void setName(String name);
    String getName();
    void ajouterCompte(CompteBancaire compte);
    void supprimerCompte(CompteBancaire compte);
    void afficherComptes();
    void deposerArgent(double montant);
    void retirerArgent(double montant) throws SoldeInsuffisantException;
}