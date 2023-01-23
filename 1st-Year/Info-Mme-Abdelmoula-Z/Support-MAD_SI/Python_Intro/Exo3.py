from simple_term_menu import TerminalMenu
nb = 0;


while True :
    print("\n-> Choissisez un nombre !")
    terminal_menu = TerminalMenu(["0","1","2","3","4","Choisire le nombre"])
    nb = terminal_menu.show()
    if nb == 5 : 
        try:
            nb = int(input("Nombre:"))
        except ValueError:
            print(chr(27) + "[2J")
            print("Merci d'utiliser des nombres")
            continue
    print(nb)
    if (0 < nb < 11):
        print("Bravo vous avez écrit un nomrbe entre 1 et 10")
        break
    else:
        print("Rater")
        