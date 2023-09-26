from Data_struct import *
import random







def print_matrix(matrix):
    for i in range(const_grille_taille):
        if i % const_racine_taille == 0 and not i == 0:
            print("_______________________\n")
        for j in range(const_grille_taille):
            if j % const_racine_taille == 0 and not j == 0:
                print(end="| ")
            print(get_val(matrix,i,j), end=" ")
        print("\n")




# (verifie si une case est vide il prende en parametre les coordonés x , y de la case) .
def box_isempty(matrix, x, y):
    return get_val(matrix,x,y) == 0





# _box_fill(x , y , v ) ( rempli la case si elle vaut 0 avec la valeur v .
# -il faut bien sur faire une petite fonction pour valider si la valeur est compris
# entre(1,9) qu'on peut l'appeler valValidation .


def box_fill(matrix, x, y, v):
    if v in range(10) and v != 0:
        matrix=set_val(matrix,x,y,v)


# la case d'une grille , rend 0 , s'il est differnt de 0.
def box_empty(matrix, x, y):
    if box_isempty(matrix, x, y):
        matrix=set_val(matrix,x,y,0)
    return matrix




# _Pour vérifier qu’une grille partielle ou complète est valide :
# -On peut faire une fonction qui valide la bloque d'abord qu'on peut l'appeler BlockValid() ,
# pour verifier si tout les membre de la bloque sont differents .
# les deux fonction ligne_debut et colonne_debut c'est pour l'utilisation dans la fonction BlockValide
# cela nous evite de parcourir toute la matrice rien que pour verfier un seul block

def line_begining(block):
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


def colon_begining(block):
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


def block_members_validation(matrix, block):
    numeros_vus = set()
    debut_ligne = line_begining(block)
    debut_colonne = colon_begining(block)
    for ligne in range(debut_ligne, debut_ligne + 3):
        for colonne in range(debut_colonne, debut_colonne + 3):
            valeur = get_val(matrix,ligne,colonne)
            if valeur in numeros_vus:
                return False
            else:
                numeros_vus.add(valeur)
    return True


# -Une fonction qui valide toute la colonne elle regarde si chaque nombre est unique dans toute la colonne ColonValid().
def colon_validation(matrix, colonne):
    numeros_vus = set()  # j'ai crée un ensemble pour qu'il sauvegarde dedans un numéro déja vu pour la prochaine verif
    for ligne in matrix:
        numero = ligne[colonne]['val']  # #RESTE A VERIFIER Si c'est comme ca ou nn  #
        # for ligne in range(9):                      #
        #  numero = get_val(matrix,ligne,colonne)     #

        if numero != 0:
            if numero in numeros_vus:
                return False
            numeros_vus.add(numero)

    return True


# -De meme Une fonction pour valider une ligne line_validation .
def line_validation(matrix, ligne):
    numeros_vus = set()  # cela me semble plus logique RESTE A VERIFIER
    for colonne in range(9):
        numero = get_val(matrix,ligne,colonne)

        if numero != 0:
            if numero in numeros_vus:
                return False  # Si le numéro est déjà apparu dans la ligne, la ligne n'est pas valide.
            numeros_vus.add(numero)  # Ajouter le numéro à l'ensemble des numéros vus.

        return True

def grid_validation(matrix):
    for ligne in matrix:
        if not line_validation(matrix, ligne):
            return False
    for colonne in matrix:
        if not colon_validation(matrix, colonne):
            return False
    for block in range(1, 10):  # la boucle elle de 1 a 9
        if not block_members_validation(matrix, block):
            return False
    return True



matrix = block_define(create_matrix(9 , struct_case))



box_fill(matrix,1 , 0 , 5)
box_fill(matrix,1 , 1 , 5)



