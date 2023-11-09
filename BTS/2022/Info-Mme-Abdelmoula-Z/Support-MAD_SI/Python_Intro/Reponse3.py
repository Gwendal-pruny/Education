print ("Bonjour tout le monde") # impresion simple
print ("Bonjour", "tout", "le", "monde", sep="-") #ajout d'un spéarateur entre chaque mots_cles
print ("Bonjour", "tout", "le", "monde", sep=" ") #ajout d'un espace entre chaque mots'
print ("Bonjour"); print ("tout le monde")# 2 impresion simple ( saut entre chaque impression )
print ("Bonjour", end=" "); print ("tout le monde") # ajout d'un espace a la fun # impresion simple


p=input("Qui est tu? >>> "); print("Bonjour"); # impresion + await for an input + impresion bonjour
p=input("Qui est tu? >>> "); print("Bonjour", p) # impresion + await for an input + impression bonjour + user input

print ("Je sais que c’est pas vrai mais j’ai 8 ans") #inspression simple
print ("Je sais que c’est pas vrai mais j’ai", 8, "ans") #impresion simple + int

i=8;
print ("Je sais que c’est pas vrai mais j’ai", i, "ans") #impresion simple + variables
j=12;
print ("Je sais que c’est pas vrai mais j’ai %d ans" %(j))#impresion simple + variables callback


i=8 ; 
j=12;
print("i et j valent respectivement %d et %d" %(i, j))#impresion simple + double variables callback
print("%d/%d=%d" %(i, j, i/j))#impresion simple + triple variables callback error 
print("%d/%d=%f"%(i,j,i/j)) #impresion simple + triple variables callback

type(p)# get type
type(i)# get type
type(j)# get type
type(i/j)# get type result
n=12/8 ; n # assigne
n=int(12/8) ; # assigne inter declaration