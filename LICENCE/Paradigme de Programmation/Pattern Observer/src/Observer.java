import java.util.ArrayList;
import java.util.List;

// Observer interface
interface Observer {
    void update(Stock stock);
}

// Concrete Observer
class Investor implements Observer {
    private String name;

    public Investor(String name) {
        this.name = name;
    }

    @Override
    public void update(Stock stock) {
        System.out.println("Investor " + this.name + " notified: Stock " + stock.getName() + " is now " + stock.getPrice());
    }
}

// Observable subject
class StockMarket {
    private List<Observer> observers = new ArrayList<>();
    private List<Stock> stocks = new ArrayList<>();

    public void addStock(Stock stock) {
        stocks.add(stock);
    }

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void updateStockPrice(String stockName, double newPrice) {
        for (Stock stock : stocks) {
            if (stock.getName().equals(stockName)) {
                stock.setPrice(newPrice);
                notifyObservers(stock);
            }
        }
    }

    private void notifyObservers(Stock stock) {
        for (Observer observer : observers) {
            observer.update(stock);
        }
    }
}

// Concrete subject
class Stock {
    private String name;
    private double price;

    public Stock(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
