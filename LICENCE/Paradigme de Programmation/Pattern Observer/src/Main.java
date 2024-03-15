public class Main {
    public static void main(String[] args) {
        StockMarket market = new StockMarket();
        Investor investor1 = new Investor("Alice");
        Investor investor2 = new Investor("Bob");

        Stock google = new Stock("Google", 2735.55);
        Stock apple = new Stock("Apple", 146.85);

        market.addStock(google);
        market.addStock(apple);

        market.addObserver(investor1);
        market.addObserver(investor2);

        market.updateStockPrice("Google", 2750.00); // Simulate a price change
        market.updateStockPrice("Apple", 150.00); // Another price change
    }
}
