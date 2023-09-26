const_grille_taille = 9
const_racine_taille = 3


def create_noteslist():
    res_list = []
    for i in range(9):
        res_list.append("True")


struct_case = {"nblock": 0, "Note_list": create_noteslist(), "val": 0}


def create_matrix(taille, struct):
    matrix = []
    for i in range(taille):
        row = [struct.copy() for _ in range(taille)]
        matrix.append(row)
    return matrix

def block_define(matrix):
    nb_block = 1
    times_nb = 0
    colon_nb = 0
    for i in range(const_grille_taille):
        for j in range(const_grille_taille):
            matrix[i][j].update({'nblock': nb_block})
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

    return matrix