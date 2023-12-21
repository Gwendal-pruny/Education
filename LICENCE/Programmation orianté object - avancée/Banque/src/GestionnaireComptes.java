import java.util.ArrayList;
import java.util.List;

public class GestionnaireComptes {
    private List<ClientBanque> clients;

    public GestionnaireComptes() {
        clients = new ArrayList<>();
    }

    public void ajouterClient(ClientBanque client) {
        clients.add(client);
    }

    public void supprimerClient(ClientBanque client) {
        clients.remove(client);
    }

    public void afficherClients() {
        for (ClientBanque client : clients) {
            client.afficherComptes();
        }
    }
    public ClientBanque findClientByName(String name) {
        for (ClientBanque client : clients) {
            if (client.getName().equals(name)) {
                return client;
            }
        }
        return null;
    }
}
// Path: src/ClientBanque.java