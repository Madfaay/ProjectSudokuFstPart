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

new_matrix = block_define(game_matrix)




# Proposition pour les fonctions de semaine 38 :

#(verifie si une case est vide il prende en parametre les coordonés x , y de la case) .
def box_isempty(matrix,x,y):
    return matrix[x][y]['val'] == 0


testbox_isempty = box_isempty(new_matrix,0,0)


#_box_fill(x , y , v ) ( rempli la case si elle vaut 0 avec la valeur v .
    #-il faut bien sur faire une petite fonction pour valider si la valeur est compris entre (1,9) qu'on peut l'appeler valValidation .


def box_fill(matrix , x , y , v):
    if v in range(10) and v != 0 :
        matrix[x][y]['val']= v


#la case d'une grille , rendre 0 , s'il est differnt de 0.
def box_empty(matrix,x,y):
    if box_isempty(matrix,x,y) :
            matrix[x][y].update({'val': 0 })
    return matrix

testbox_empty = box_empty(new_matrix,0,0)

#_Pour vérifier qu’une grille partielle ou complète est valide :
 #-On peut faire une fonction qui valide la bloque d'abord qu'on peut l'appeler BlockValid() , pour verifier si tout les membre de la bloque sont differents .

# les deux fonction ligne_debut et colonne_debut c'est pour l'utilisation dans la fonction BlockValide ca nous evite de parcourir toute la matrice rien que pour verfier un seul block

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


def block_members_validation (matrix  , block):
    numeros_vus = set()
    debut_ligne  = line_begining(block)
    debut_colonne = colon_begining(block)
    for ligne in range(debut_ligne, debut_ligne + 3):
        for colonne in range(debut_colonne, debut_colonne + 3):
            valeur = matrix[ligne][colonne]['val']
            if valeur in numeros_vus: 
                return False
            else:
                numeros_vus.add(valeur)
    return True


 #-Une fonction qui valide toute la colonne elle regarde si chaque nombre est unique dans toute la colonne ColonValid().
def colon_validation(matrix, colonne):
    numeros_vus = set() # j'ai crée un ensemble pour qu'il sauvegarde dedans un numéro déja vu pour la prochaine verif
    for ligne in matrix:
        numero = ligne[colonne]['val']
        if numero != 0:
            if numero in numeros_vus:
                return False  
            numeros_vus.add(numero)  

    return True

 #-De meme Une fonction pour valider une ligne line_validation .
def line_validation(matrix, ligne):
    numeros_vus = set()  
    for numero in matrix[ligne]:
        if numero != 0:
            if numero in numeros_vus:
                return False  # Si le numéro est déjà apparu dans la ligne, la ligne n'est pas valide.
            numeros_vus.add(numero)  # Ajouter le numéro à l'ensemble des numéros vus.

    return True


def GrilleValid (matrix) :
    for ligne in matrix :
        if line_validation(matrix,ligne)== False:
            return False
    for colonne in matrix:
        if colon_validation(matrix,colonne) ==  False :
            return False
    for block in range(1,10): # la boucle elle de 1 a 9
        if block_members_validation(matrix, block)==False :
            return False
    return True