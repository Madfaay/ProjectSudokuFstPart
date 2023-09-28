const_grille_taille = 9
const_racine_taille = 3


def create_noteslist() :
    """
    La fonction create_note_list nous permet de créer une liste composée de 9 booléens
    initialisé à True.
    :return:liste de booléens

    """
    res_list = []
    for i in range(9):
        res_list.append(True)
    return res_list


struct_case = {"nblock": 0, "Note_list": create_noteslist(), "val": 0}


def create_matrix(taille, struct) -> list[list[struct_case]]:
    """
    La fonction create_matrix nous permet de créer la matrice correspondant à la grille du jeu.

    :param taille: La taille de la matrice supposée être 9.
    :type taille: int
    :param struct: La structure qui représente la case.
    :type struct: struct_case
    :return: Une liste bidimensionnelle où chaque case contient la structure (struct_case).
    :rtype: List[List[struct_case]]
    """
    matrix = []
    for i in range(taille):
        row = [struct.copy() for _ in range(taille)]
        matrix.append(row)
    return matrix



#permet de récupérer la valeur'nblock' de struct_case


def get_nblock(matrix,x,y):
    """
    La fonction get_nblock permet de récupérer la valeur 'nblock' de struct_case.
    :param matrix: La matrice qui contient les cases structurées.
    :type matrix: list[list[struct_case]]
    :param x: L'abscisse de la case.
    :type x: int
    :param y: L'ordonnée de la case.
    :type y: int
    :return: Le numéro du bloc pour la case concernée.
    :rtype: int
    """

    return matrix[x][y]['nblock']

#permet de modifier la valeur 'nblock' de struct_case
def set_nblock(matrix,x,y,nb_block):
    """
      La fonction set_nblock permet d'affecter une valeur au champ 'nblock' de struct_case.
      :param matrix: La matrice qui contient les cases structurées.
      :type matrix: list[list[struct_case]]
      :param x: L'abscisse de la case.
      :type x: int
      :param y: L'ordonnée de la case.
      :type y: int
      :param nb_block: le numero de bloque.
      :type nb_block: int
      :return: un void .
      """
    matrix[x][y].update({'nblock': nb_block})


def get_note(matrix,x,y):
    """
      La fonction get_note permet de récupérer la liste 'Note_list' contenu dans struct_case.
      :param matrix: La matrice qui contient les cases structurées.
      :type matrix: list[list[struct_case]]
      :param x: L'abscisse de la case.
      :type x: int
      :param y: L'ordonnée de la case.
      :type y: int
      :return: une liste de booléens .
      :rtype: list[bool]
      """
    return matrix[x][y]['Note_list']


def rem_note(matrix,x,y,id):
    """
         La fonction rem_note permet de modifier un élement la liste 'Note_list' contenu dans struct_case.
         :param matrix: La matrice qui contient les cases structurées.
         :type matrix: list[list[struct_case]]
         :param x: L'abscisse de la case.
         :type x: int
         :param y: L'ordonnée de la case.
         :type y: int
         :param id: l'indice de l'élement de la liste.
         :type id: int
         :return: une liste de booléens .
         :rtype: list[bool]
         """
    matrix[x][y]['Note_liste'][id - 1] = False



#permet de récupérer l'élément 'val' de struct_case
def get_val(matrix,x,y):
    """
            La fonction get_val permet de récupérer l'élément 'val' de struct_case
            :param matrix: La matrice qui contient les cases structurées.
            :type matrix: list[list[struct_case]]
            :param x: L'abscisse de la case.
            :type x: int
            :param y: L'ordonnée de la case.
            :type y: int
            :return: la valeur de la case qui est 0 si null ou autre < 9 .
            :rtype: int
            """
    return matrix[x][y]['val']

#permet de modifier la valeur 'val' de struct_case
def set_val(matrix,x,y,val):
    """
       La fonction set_val permet d'affecter une valeur au champ 'val' de struct_case.
       :param matrix: La matrice qui contient les cases structurées.
       :type matrix: list[list[struct_case]]
       :param x: L'abscisse de la case.
       :type x: int
       :param y: L'ordonnée de la case.
       :type y: int
       :param val: la valeur qu'on veut affecter à la case.
       :type val: int
       :return: rien elle fait juste la modification.
       :rtype: void .

       """
    matrix[x][y].update({'val': val})



def block_define(matrix):
    """
La fonction block_define permet d'affecter un numéro de bloc au champ 'n_block' de struct_case.
Cet algorithme n'est pas encore définitif. Nous avons tenté de trouver un algorithme qui remplit les numéros de cases
avec une précision, en ignorant pour l'instant le fait qu'une formule plus efficace puisse être trouvée,
afin de fusionner cette opération avec create_matrix, évitant ainsi un second parcours de la matrice après sa création.

Voir aussi:
    - :func:`create_matrix`: Documentation de la fonction create_matrix.

:param matrix: La matrice qui contient les cases structurées.
:type matrix: list[list[struct_case]]
:return: Aucune valeur n'est renvoyée, la fonction effectue simplement des modifications sur chaque case.
:rtype: None

       """
    nb_block = 1
    times_nb = 0
    colon_nb = 0
    for i in range(const_grille_taille):
        for j in range(const_grille_taille):
            set_nblock(matrix,i,j,nb_block)
            times_nb += 1
            if times_nb % const_racine_taille == 0 and times_nb != 0 and times_nb != const_grille_taille and colon_nb < const_racine_taille:
                nb_block += 1
            else:
                if nb_block % const_racine_taille == 0 and colon_nb < const_racine_taille and times_nb % const_racine_taille == 0:
                    nb_block += 1
            if times_nb == const_grille_taille:
                if colon_nb == 2:
                    colon_nb = 0
                    times_nb = 0
                else:
                    nb_block -= const_racine_taille
                    times_nb = 0
                    colon_nb += 1

