public class Main {
    public static void main(String[] args) {
        GestionnaireComptes gestionnaire = new GestionnaireComptes();

        CompteEpargne compteEpargne = new CompteEpargne();
        CompteCourant compteCourant = new CompteCourant();

        ClientBanque client = new ClientBanqueImpl();
        client.setName("John Doe");
        client.setId(123);
        client.ajouterCompte(compteEpargne);
        client.ajouterCompte(compteCourant);

        gestionnaire.ajouterClient(client);

        try {
            compteEpargne.deposerArgent(1000);
            compteCourant.deposerArgent(500);

            compteEpargne.retirerArgent(200);
            compteCourant.retirerArgent(300);

            // Simuler une exception de solde insuffisant
            compteEpargne.retirerArgent(1500);
        } catch (SoldeInsuffisantException e) {
            System.out.println("Exception : " + e.getMessage());
        }
        client.afficherComptes();
        UserInterface ui = new UserInterface();
        ui.start();
    }

}