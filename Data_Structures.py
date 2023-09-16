

struct_case = {"nGrp": 0, "Note_list": [], "val": 0}

def create_matrix(taille , struct):
    current_length = 0
    matrix = []
    liste_vide = []
    while current_length < taille:
        matrix.append(liste_vide)
        current_length += 1
    current_length = 0
    block_nmb= 1
    line_indice = 1
    nbr_fois = 1
    for grille in matrix:

        while current_length < taille:
            if nbr_fois == 3:
                nbr_fois = 1
                block_nmb += 1
            if line_indice % 9 == 0 :
               line_indice = 1
               nbr_fois += 1

            else :
                if line_indice % 3 == 0:
                  print(line_indice)
                  block_nmb += 1
            new_element = struct
            struct["nGrp"] = block_nmb
            print(block_nmb)
            grille.append(struct)
            line_indice+= 1
            current_length += 1
    current_length = 0
    return matrix





#
game_matrix = create_matrix(9 , struct_case)
print(game_matrix)
#Proposition pour les fonctions de semaine 38 :

#_boxIsEmpty(x , y) (verifie si une case est vide il prende en parametre les coordonés x , y de la case) .

#_boxFill(x , y , v ) ( rempli la case si elle vaut 0 avec la valeur v .
    #-il faut bien sur faire une petite fonction pour valider si la valeur est compris entre (1,9) qu'on peut l'appeler valValidation .

#BoxEmpty(x , y ) vider la case d'une grille , rendre 0 , s'il est differnt de 0 .

#_Pour vérifier qu’une grille partielle ou complète est valide :
 #-On peut faire une fonction qui valide la bloque d'abord qu'on peut l'appeler BlockValid() , pour verifier si tout les membre de la bloque sont differents .
 #-Une fonction qui valide toute la colonne elle regarde si chaque nombre est unique dans toute la colonne ColonValid().
 #-De meme Une fonction pour valider une ligne LineValid() .