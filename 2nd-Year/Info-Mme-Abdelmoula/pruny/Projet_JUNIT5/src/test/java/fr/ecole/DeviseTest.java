package fr.ecole;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

class DeviseTest {

    @Test
    void add() {
        // ici on teste la méthode add
    }

    @Test
    void testEquals() {

        Devise dc45= new Devise(45,"Dollar Canadien");
        Devise dc65= new Devise(65,"Dollar Canadien");
        LocalDate mauvaisD= LocalDate.now();// appel d'une méthode statique
        Devise euro45= new Devise(45,"Euro");;

        //ici on teste la méthode equals
        // tests réalisés
        // d et d2 égaux
        // première comparaison entre 2 objets égaux
        boolean result = dc45.equals(dc45);
        boolean resAttendue= false;
        Assertions.assertEquals(resAttendue,result,"égalité devrait être constatée");

        // quantité de d différente de d2
        // monnaie de d différente de d2
        // qté et monnaie différente de d1 et d2
        // d2 pas une Devise
        // d2 est null

    }
}