import java.util.Scanner;

public class UserInterface {
    private GestionnaireComptes gestionnaire;
    private Scanner scanner;

    public UserInterface() {
        gestionnaire = new GestionnaireComptes();
        scanner = new Scanner(System.in);
    }

    public void start() {
        while (true) {

            System.out.println("1. Create account");
            System.out.println("2. Deposit money");
            System.out.println("3. Withdraw money");
            System.out.println("4. Delete account");
            System.out.println("5. Check balance");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over
            switch (option) {
                case 1:
                    createAccount();
                    break;
                case 2:
                    depositMoney();
                    break;
                case 3:
                    withdrawMoney();
                    break;
                case 4:
                    deleteAccount();
                    break;
                case 5:
                    checkBalance();
                    break;
                case 6:
                    System.out.println("Goodbye!");
                    return;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }

    private void createAccount() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Choose account type (1 for Courant, 2 for Epargne): ");
        int accountType = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over
        ClientBanque client = new ClientBanqueImpl();
        client.setName(name);
        if (accountType == 1) {
            CompteCourant compteCourant = new CompteCourant();
            client.ajouterCompte(compteCourant);
        } else if (accountType == 2) {
            CompteEpargne compteEpargne = new CompteEpargne();
            client.ajouterCompte(compteEpargne);
        } else {
            System.out.println("Invalid account type. Please try again.");
            return;
        }
        gestionnaire.ajouterClient(client);
        System.out.println("Account created successfully.");
    }

    private void checkBalance() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        ClientBanque client = gestionnaire.findClientByName(name);
        if (client == null) {
            System.out.println("Client not found.");
            return;
        }
        client.afficherComptes();
    }

    private void depositMoney() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        ClientBanque client = gestionnaire.findClientByName(name);
        if (client == null) {
            System.out.println("Client not found.");
            return;
        }
        System.out.print("Enter the amount to deposit: ");
        double amount = scanner.nextDouble();
        scanner.nextLine(); // Consume newline left-over
        client.deposerArgent(amount);
        System.out.println("Money deposited successfully.");
    }

    private void withdrawMoney() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        ClientBanque client = gestionnaire.findClientByName(name);
        if (client == null) {
            System.out.println("Client not found.");
            return;
        }
        System.out.print("Enter the amount to withdraw: ");
        double amount = scanner.nextDouble();
        scanner.nextLine(); // Consume newline left-over
        try {
            client.retirerArgent(amount);
            System.out.println("Money withdrawn successfully.");
            checkBalance();
        } catch (SoldeInsuffisantException e) {
            System.out.println("Insufficient balance.");
        }
    }

    private void deleteAccount() {
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        ClientBanque client = gestionnaire.findClientByName(name);
        if (client == null) {
            System.out.println("Client not found.");
            return;
        }
        gestionnaire.supprimerClient(client);
        System.out.println("Account deleted successfully.");
    }

}