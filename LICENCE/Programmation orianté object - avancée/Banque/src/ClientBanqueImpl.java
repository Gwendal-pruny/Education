import java.util.ArrayList;
import java.util.List;

public class ClientBanqueImpl implements ClientBanque {
    private int id;
    private String name;
    private List<CompteBancaire> comptes;

    public ClientBanqueImpl() {
        this.comptes = new ArrayList<>();
    }

    @Override
    public void setId(int id) {
        this.id = id;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void ajouterCompte(CompteBancaire compte) {
        comptes.add(compte);
        System.out.println("Compte ajouté pour le client.");
    }

    @Override
    public void supprimerCompte(CompteBancaire compte) {
        comptes.remove(compte);
        System.out.println("Compte supprimé pour le client.");
    }

    @Override
    public void afficherComptes() {
        for (CompteBancaire compte : comptes) {
            System.out.println("Balance: " + compte.consulterSolde());
        }
    }

    @Override
    public void deposerArgent(double montant) {
        // Implementation of deposerArgent
    }

    @Override
    public void retirerArgent(double montant) throws SoldeInsuffisantException {
        // Implementation of retirerArgent
    }
}