# Pattern Builder
## Description
Le pattern Builder permet de construire des objets complexes étape par étape. Il sépare la construction d'un objet complexe de sa représentation, permettant ainsi le même processus de construction de produire différents types et représentations d'objets.

## Mise en œuvre
Dans notre exemple de gestion de commandes de café (CoffeeOrderBuilder), ce pattern est utilisé pour créer des instances de la classe CoffeeOrder. Le builder permet aux utilisateurs de spécifier le type de café, si du lait ou du sucre doivent être ajoutés, et d'autres extras, puis construit l'objet CoffeeOrder correspondant.

```java
public class CoffeeOrderBuilder {
    private String type;
    private boolean milk;
    private boolean sugar;
    private String extras;
    public CoffeeOrderBuilder setType(String type) { ... }
    public CoffeeOrderBuilder setMilk(boolean milk) { ... }
    public CoffeeOrderBuilder setSugar(boolean sugar) { ... }
    public CoffeeOrderBuilder setExtras(String extras) { ... }
    public CoffeeOrder build() { ... }
}
```

Le client (dans ce cas, Main.java) utilise le CoffeeOrderBuilder pour créer diverses configurations de CoffeeOrder, démontrant la flexibilité et la puissance du pattern Builder.

# Pattern Command
## Description
Le pattern Command transforme une requête en un objet autonome qui contient toutes les informations nécessaires à la requête. Ce pattern permet de paramétrer des méthodes avec des requêtes, de mettre en file d'attente ou de logger des requêtes, et de supporter des opérations annulables.

## Mise en œuvre
Nous avons utilisé ce pattern dans un système de contrôle d'éclairage intelligent où des commandes (Command) contrôlent l'état des lumières (Light). Chaque commande implémente une interface Command qui définit une méthode execute() et une méthode undo().

```java
interface Command {
    void execute();
    void undo();
}

class TurnOnLightCommand implements Command { ... }
class TurnOffLightCommand implements Command { ... }
class AdjustBrightnessCommand implements Command { ... }
```

Les commandes sont utilisées par le LightControlPanel pour modifier l'état des Light et peuvent être annulées ou réexécutées facilement.

# Pattern Decorator
## Description
Le pattern Decorator permet d'ajouter de nouvelles fonctionnalités à des objets en les plaçant à l'intérieur d'objets enveloppe spéciaux. Cela fournit une alternative flexible au sous-classement pour étendre les fonctionnalités.

## Mise en œuvre
Dans le système de café personnalisable, chaque décorateur (Decorator) étend une classe abstraite Decorateur qui implémente l'interface Boisson. Chaque décorateur modifie le comportement de la méthode description() ou cout().

```java
abstract class Decorateur implements Boisson {
    protected Boisson boisson;
    public Decorateur(Boisson boisson) { ... }
}

class Lait extends Decorateur { ... }
class Sucre extends Decorateur { ... }
class Caramel extends Decorateur { ... }
```

Les décorateurs peuvent être empilés les uns sur les autres, permettant ainsi de combiner plusieurs fonctionnalités de manière dynamique.

# Pattern Observer
## Description
Le pattern Observer permet à un objet de notifier automatiquement ses dépendances, appelées observateurs, de tout changement d'état.

## Mise en œuvre
Dans notre système de suivi de stocks, StockMarket agit comme un sujet observable et Investor comme un observateur. Les investisseurs s'abonnent au marché boursier et sont notifiés de tout changement dans le prix des actions.

```java
interface Observer {
    void update(Stock stock);
}

class StockMarket {
    private List<Observer> observers;
    public void addObserver(Observer observer) { ... }
    public void removeObserver(Observer observer) { ... }
    public void updateStockPrice(String stockName, double newPrice) { ... }
}
```

Lorsque StockMarket modifie le prix d'une action, il notifie tous les observateurs enregistrés en appelant leur méthode update().

# Pattern Singleton
## Description
Le pattern Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global à cette instance.

## Mise en œuvre
Dans l'implémentation de l'ArbreBinaire, le singleton est utilisé pour créer une instance unique d'un arbre vide. Cela garantit que toutes les références à l'arbre vide pointent vers le même objet, ce qui est crucial pour vérifier si un nœud de l'arbre est vide.

```java
public class ArbreBinaire {
    private static final ArbreBinaire arbreVide = new ArbreBinaire();
    private ArbreBinaire() { ... } // Constructeur privé
    public static ArbreBinaire creer() { return arbreVide; }
}
```

Le pattern Singleton est particulièrement utile dans les cas où un contrôle strict sur les ressources est nécessaire, comme avec l'arbre vide dans notre structure d'arbre binaire.

-------------


### Chaque pattern de conception est utilisé pour résoudre des problèmes spécifiques dans le développement logiciel, offrant des solutions éprouvées pour les défis courants en matière de conception de logiciels.