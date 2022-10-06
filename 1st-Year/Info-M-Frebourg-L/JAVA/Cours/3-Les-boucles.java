//Écrire un programme qui saisit deux entiers et qui incrémente de 1 le premier tant qu’il n’est pas supérieur au deuxième.

import java.util.Scanner;

class Questions7 {
    public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);
    System.out.println("Veuillez saisir le premier nombre :");
    int i = sc.nextInt();
    System.out.println("Veuillez saisir le second nombre :");
    int j = sc.nextInt();

    while(j <= i);
        i++;
        System.out.println(i);

    }


}

// Afficher les nombres pairs de 0 à 20 dans l’ordre décroissant

class Question8 {
    public static void main(String[] args) {

        for (int indice = 20; indice >= 0;) {
            System.out.print(indice);
            indice  = indice - 2;
        }
    }
}

// Que fait cette boucle ?
// Tant que indice est >= 0 on retire 2 a indice et on l'imprime 

// Afficher pour chaque nombre de 1 à 10 les nombres qui lui précédent .

public class Question10 {
    public static void main(String[] args) {
        
        for (int mainnombre = 1; mainnombre <= 10;) {
            int nombre = mainnombre;
            for (nombre > 0; nombre++){
                System.out.println(nombre);
            }
            mainnombre = mainnombre + 1;
            }
        }
}

// Écrire un programme qui saisit un entier positif.
// Écrire un programme qui affiche n fois ‘coucou’, l’entier n sera saisi par l’utilisateur.
// Écrire un programme qui saisit un nombre tant qu’il n’est pas égal à 10.
// Écrire un programme qui saisit un nombre tant qu’il n’est pas égal à 10 et affiche un message du style ‘ce nombre n’est pas bon’.
 