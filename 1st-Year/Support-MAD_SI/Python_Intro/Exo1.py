#Import
from simple_term_menu import TerminalMenu

# Déclaration de toute les variables utiliser

nb = 0;

# escape sequences
print(chr(27) + "[2J")

# Introduction
print("・．━━━━━━━━━━━━━━━━━━━━━ † ━━━━━━━━━━━━━━━━━━━━━．・")
print("★░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░★")
print("★░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░★")
print("★░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░★")
print("★░░░░░░░███████░░░░░░░██░░░░░░░░░░░░★")
print("★░░░░█████░░░░░░░░░░░░░░███░██░░░░░░★")
print("★░░░██░░░░░████░░░░░░░░░░██████░░░░░★")
print("★░░░██░░████░░███░░░░░░░░░░░░░██░░░░★")
print("★░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░★")
print("★░░░░██████████░███░░░░░░░░░░░██░░░░★")
print("★░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░★")
print("★░░░░███████████░░██░░░░░░░░░░██░░░░★")
print("★░░░░░░██░░░░░░░████░░░░░██████░░░░░★")
print("★░░░░░░██████████░██░░░░███░██░░░░░░★")
print("★░░░░░░░░░██░░░░░████░███░░░░░░░░░░░★")
print("★░░░░░░░░░█████████████░░░░░░░░░░░░░★")
print("★░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░★")
print("・．━━━━━━━━━━━━━━━━━━━━━ † ━━━━━━━━━━━━━━━━━━━━━．・")


print("\nBienvenue sur mon super detecteur de nombre pair ! wao !.")

while True :
    print("\n-> Choissisez un nombre !")
    terminal_menu = TerminalMenu(["0","1","2","3","4","Choisire le nombre"])
    nb = terminal_menu.show()
    if nb == 5 :
        try:
            nb = int(input("Nombre:"))
            break
        except ValueError:
            print(chr(27) + "[2J")
            print("Merci d'utiliser des nombres")
            continue
    print(nb)
    break

if (nb % 2) == 0:
   print("{0} est Paire".format(nb))
else:
   print("{0} est Impaire".format(nb))


