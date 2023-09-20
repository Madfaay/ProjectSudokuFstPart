struct_case = {"nblock": 0, "Note_list": [], "val": 0}


def create_matrix(taille, struct):
    matrix = []
    for i in range(taille):
        row = [struct.copy() for j in range(taille)]
        matrix.append(row)
    return matrix


def block_define(matrix):
    nb_block = 1
    times_nb = 0
    colon_nb = 0
    for i in range(9):
        for j in range(9):
            matrix[i][j].update({'nblock': nb_block})
            times_nb += 1
            print(matrix[i][j])

            if times_nb % 3 == 0 and times_nb != 0 and times_nb != 9 and colon_nb < 3:
                nb_block += 1
            else:
                if nb_block % 3 == 0 and colon_nb < 3 and times_nb % 3 == 0:
                    nb_block += 1
            if times_nb == 9:
                if colon_nb == 2:
                    colon_nb = 0
                    times_nb = 0
                else:
                    nb_block -= 3
                    times_nb = 0
                    colon_nb += 1

    return matrix

game_matrix = create_matrix(9, struct_case)
print(game_matrix)

new_matrix = block_define(game_matrix)

print(new_matrix)



# Proposition pour les fonctions de semaine 38 :

#(verifie si une case est vide il prende en parametre les coordonés x , y de la case) .
def box_isempty(matrix,x,y):
    return matrix[x][y]['val'] == 0


testbox_isempty = box_isempty(new_matrix,0,0)

print(testbox_isempty)

#_boxFill(x , y , v ) ( rempli la case si elle vaut 0 avec la valeur v .
    #-il faut bien sur faire une petite fonction pour valider si la valeur est compris entre (1,9) qu'on peut l'appeler valValidation .


#la case d'une grille , rendre 0 , s'il est differnt de 0 .
def box_empty(matrix,x,y):
    if box_isempty(matrix,x,y) :
            matrix[x][y].update({'val': 0 })
    return matrix

testbox_empty = box_empty(new_matrix,0,0)
print(testbox_empty)

#_Pour vérifier qu’une grille partielle ou complète est valide :
 #-On peut faire une fonction qui valide la bloque d'abord qu'on peut l'appeler BlockValid() , pour verifier si tout les membre de la bloque sont differents .
 #-Une fonction qui valide toute la colonne elle regarde si chaque nombre est unique dans toute la colonne ColonValid().
 #-De meme Une fonction pour valider une ligne LineValid() .