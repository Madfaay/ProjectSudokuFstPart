from Data_struct import *
import random


def print_matrix(matrix) :
    """
La fonction print_matrix permet d'afficher la matrice.
:param matrix: La matrice qui contient les cases structurées.
:type matrix: list[list[struct_case]]
:return: Aucune valeur n'est renvoyée, la fonction effectue simplement un affichage .
:rtype: None

       """
    for i in range(const_grille_taille):
        if i % const_racine_taille == 0 and not i == 0:
            print("_______________________\n")
        for j in range(const_grille_taille):
            if j % const_racine_taille == 0 and not j == 0:
                print(end="| ")
            print(get_val(matrix,i,j), end=" ")
        print("\n")




def box_isempty(matrix, x, y):
    """
    :param matrix: La matrice qui contient les cases structurées.
    :type matrix: list[list[struct_case]]
    :param x: L'abscisse de la case.
    :type x: int
    :param y: L'ordonnée de la case.
    :type y: int
    :return: True c'est la case posséde 0 comme valeur , pour une autre valaure c'est False .
    :rtype: bool

       """

    return get_val(matrix,x,y) == 0







def box_fill(matrix, x, y, v) -> None:
    """
    La fonction box_fill remplie la case s'elle vaut 0 avec la valeur v
    :param matrix: La matrice qui contient les cases structurées.
    :type matrix: list[list[struct_case]]
    :param x: L'abscisse de la case.
    :type x: int
    :param y: L'ordonnée de la case.
    :type y: int
    :param v: la valeur qu'on veut l'affecter à la case.
    :type v: int
    :return: Rien elle fait juste une modification.
    :rtype: void

       """
    if v in range(10) and v != 0:
        set_val(matrix,x,y,v)


# la case d'une grille , rend 0 , s'il est differnt de 0.
def box_empty(matrix, x, y):
    """
     La fonction box_empty remplie la case d'une grille avec la valeur 0 si ce n'est pas déja fait .
     :param matrix: La matrice qui contient les cases structurées.
     :type matrix: list[list[struct_case]]
     :param x: L'abscisse de la case.
     :type x: int
     :param y: L'ordonnée de la case.
     :type y: int
     :return: Rien elle fait juste une modification.
     :rtype: void

        """
    if not box_isempty(matrix, x, y):
        set_val(matrix,x,y,0)




# _Pour vérifier qu’une grille partielle ou complète est valide :
# -On peut faire une fonction qui valide la bloque d'abord qu'on peut l'appeler BlockValid() ,
# pour verifier si tout les membre de la bloque sont differents .
# les deux fonction ligne_debut et colonne_debut c'est pour l'utilisation dans la fonction BlockValide
# cela nous evite de parcourir toute la matrice rien que pour verfier un seul block

def line_begining(block):
    """
        La fonction 'line_begining' prend en paramètre un bloc et retourne la première ligne de ce bloc
        :param block: L'abscisse de la case.
        :type block: int
        :return: retourne la première ligne de ce bloc.
        :rtype: void

           """
    result = None  # Initialisez la variable result à une valeur par défaut

    if block >= 1:
        if block <= 3:
            result = 0
        elif block <= 6:  # Utilisez "elif" pour éviter des conditions inutiles
            result = 3
        elif block <= 9:
            result = 6
        else:
            print("Le bloc est invalide")
    else:
        print("Le bloc est invalide")

    return result


def colon_begining(block):
    """
        La fonction 'colon_begining' prend en paramètre un bloc et retourne la première colonne de ce bloc
        :param block: l'ordonnée de la case.
        :type block: int
        :return: retourne la première colonne de ce bloc.
        :rtype: void

           """
    result = None  # Initialisez la variable result à une valeur par défaut

    if block % 3 == 0:
        result = 6
    elif block % 3 == 2:
        result = 3
    elif block % 3 == 1:
        result = 0
    else:
        print("Block invalide")

    return result


def block_members_validation(matrix, block):
    """
        La fonction 'block_members_validatio' prend une matrice en paramètre et vérifie si elle est valide ou non.
        Si toutes les lignes, colonnes et blocs sont valides, alors la grille est considérée comme valide, sinon non
        :param matrix: La matrice qui contient les cases structurées.
         :type matrix: list[list[struct_case]]
         :param block: numero de block.
         :type block: int
         :return : un booléen True si le block est valide False sinon
         :rtype : bool


                 """
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

# -Une
def colon_validation(matrix, colonne):
    """
     La fonction colon_validation valide toute la colonne elle regarde si chaque nombre est unique dans toute la colonne .
     :param matrix: La matrice qui contient les cases structurées.
     :type matrix: list[list[struct_case]]
     :colonne x: L'abscisse de la case.
     :type colonne: int
     :return: True c'est la colonne est valide , False sinon .
     :rtype: bool

        """
    numeros_vus = set()  # j'ai crée un ensemble pour qu'il sauvegarde dedans un numéro déja vu pour la prochaine verif
    for ligne in matrix:
        numero = ligne[colonne]['val']
        if numero != 0:
            if numero in numeros_vus:
                return False
            numeros_vus.add(numero)

    return True
# -De meme Une fonction pour valider une ligne line_validation .
def line_validation(matrix, ligne):
    """
        La fonction line_validation valide toute la ligne elle regarde si chaque nombre est unique dans toute la ligne .
        :param matrix: La matrice qui contient les cases structurées.
        :type matrix: list[list[struct_case]]
        :colonne x: L'abscisse de la case.
        :type colonne: int
        :return: True c'est la ligne est valide , False sinon .
        :rtype: bool

           """
    numeros_vus = set()
    for colonne in range(9):
        numero = get_val(matrix,ligne,colonne)
        #print(numero)

        if numero != 0:
            if numero in numeros_vus:
                return False  # Si le numéro est déjà apparu dans la ligne, la ligne n'est pas valide.
            numeros_vus.add(numero)  # Ajouter le numéro à l'ensemble des numéros vus.

    return True
 
def grid_validation(matrix):
    """
    La fonction 'grid_validation' prend une matrice en paramètre et vérifie si elle est valide ou non.
    Si toutes les lignes, colonnes et blocs sont valides, alors la grille est considérée comme valide, sinon non.
    :param matrix: La matrice qui contient les cases structurées.
    :type matrix: list[list[struct_case]]
    :return: True si la grille est valide, False sinon.
    :rtype: bool

    """
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






