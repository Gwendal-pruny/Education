
from simple_term_menu import TerminalMenu

def exo3():
    ab = "Les lettre A seront remplacer par la lettre b aaaaAAAA bbbbBBBB"
    new_ab = ab.replace('A','b')
    print(new_ab)
    
def exo4():
    mon_tableau = []
    k = int(input("Donnez un entier N : "))
    while k >= 1:
        k = k - 1
        print(k)
        try:
            valeur = int(input("Donnez une valeur : "))
            mon_tableau.append(valeur)
        except ValueError:
            print(chr(27)+ "[2J")
            print("Merci d'utiliser des nombres")
            break
        
    for element in mon_tableau:
        print(element)
        

def exo5(tableau):
    max_value = None
    for num in tableau:
        if (max_value is None or num > max_value):
            max_value = num
        print('Maximum value:', max_value)

def exo6(tableau):
    moyenne = sum(tableau)/len(tableau)
    print(moyenne)
    
def exo7():
    while True:
        print("\nLanguage: francais, english")
        terminal_menu = TerminalMenu(["fr", "en"])
        language = terminal_menu.show()
        if language == 0 :
            nom = input("Donnez votre nom : ")
            prenom = input("Donnez votre prenom : ")
            print("\nBonjour " + nom +" "+ prenom) 
        else:
            nom = input("Give your surname : ")
            prenom = input("Give your name : ")
            print("\nWelcome " + nom +" "+ prenom)

def exo8(tab):
    vu = [False]*len(tab)
    for i in range(len(tab)):
        if not vu[i]:
            compteur = 0
            for j in range(i, len(tab)):
                if tab[j] == tab[i]:
                    vu[j] = True
                    compteur += 1
            print(str(tab[i])+" a "+str(compteur)+" occurrences");