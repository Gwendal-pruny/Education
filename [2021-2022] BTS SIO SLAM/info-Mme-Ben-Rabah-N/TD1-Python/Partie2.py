def premierTest(k):
    if k > 1:
        for i in range(2, int(k/2)+1):
            if (k % i) == 0:
                print("votre nombre n'est pas un nombre premier")
                break
        else:
            print("votre nombre es un nombre premier")

    else:
        print("votre nombre n'est pas un nombre premier")
         
         
         
         
k = int(input("Donnez un entier : "))
premierTest(k)