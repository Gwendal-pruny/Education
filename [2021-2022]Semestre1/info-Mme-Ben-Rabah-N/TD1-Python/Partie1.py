from simple_term_menu import TerminalMenu

def ligne(nombre):
    for i in range (nombre):
        print("*", end="")
        
def carreplein(nombre):
    for i in range (nombre):
        print("*" * nombre)
        
# def croix(nombre):
#     print("*" + nombre -)

def carrecreux(nombre):
    for i in range(nombre) :
        for j in range (nombre):
            if i == 0 or i == nombre - 1:
                print("*", end="")
            else:
                if j == 0 or j == nombre - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()
        
        
def triangleplein(nombre) :   
    for i in range (1,nombre+1):
        s=''
        for j in range(1,i+1):
            s+="*"
        print(s)
        
def draw():
    while True:
        nombre = 0
        print("\nSaisissez un nombre")
        terminal_menu = TerminalMenu(["0","1","2","3","4","Choisire le nombre"])
        nombre = terminal_menu.show()
        if nombre == 5 :
            try:
                nombre = int(input("Nombre choisit :"))
                forme(nombre)
            except ValueError:
                print(chr(27) + "[2J")
                print("Merci d'utiliser des nombres")
                break     
        else:
            forme(nombre)
def forme(nombre):
        forme = 0
        print("\nSaisissez une forme")
        terminal_menu = TerminalMenu(["Ligne","Carré plein","Triangle plein","Carré creux","Croix"])
        forme = terminal_menu.show()
        if forme == 0 :
            ligne(nombre)
        elif forme == 1 :
            carreplein(nombre)
        elif forme == 2 :
            triangleplein(nombre)
        elif forme == 3 :
            carrecreux(nombre)
        elif forme == 4 :
            croix(nombre)
            
            
draw()
    