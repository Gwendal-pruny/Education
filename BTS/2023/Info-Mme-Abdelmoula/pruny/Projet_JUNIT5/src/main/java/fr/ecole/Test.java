package fr.ecole;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class Test {

    public static void main(String[] args){
        Devise d= new Devise(45,"Dollar Canadien");
        Devise d2= new Devise(65,"Dollar Canadien");
        LocalDate date= LocalDate.now();// appel d'une méthode statique
        Devise d3= null;
        if(d.equals(d3)) {
            System.out.println("youppi c'est égal");
        }
        else {
            System.out.println("c'est pas égal");
        }

        // tests réalisés
        // d et d2 égaux
        // quantité de d différente de d2
        // monnaie de d différente de d2
        // d2 pas une Devise
        // d2 est null

    }
}
