def ligne_debut(block):
    result = None  # Initialisez la variable result à une valeur par défaut

    if block >= 1:
        if block <= 3:
            result = 1
        elif block <= 6:  # Utilisez "elif" pour éviter des conditions inutiles
            result = 2
        elif block <= 9:
            result = 3
        else:
            print("Le bloc est invalide")
    else:
        print("Le bloc est invalide")

    return result 


def colonne_debut(block):
    result = None  # Initialisez la variable result à une valeur par défaut

    if block % 3 == 0:
        result = 7
    elif block % 3 == 2:
        result = 4
    elif block % 3 == 1:
        result = 1
    else:
        print("Block invalide")

    return result 



def aff (n):
    for i in range(n):
        print(i)

aff(9)



