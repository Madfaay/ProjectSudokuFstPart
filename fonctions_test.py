from Data_Structures import *

def test_create_matrix():
    struct_case = {"nblock": 0, "Note_list": create_noteslist(), "val": 0}
    taille = 3
    matrix = create_matrix(taille, struct_case)
    assert len(matrix) == taille
    for row in matrix:
        assert len(row) == taille
        for element in row:
            assert element == struct_case


def test_create_noteList() :
        test_list = [True, True, True, True, True, True, True, True, True]
        assert test_list == create_noteslist()


def test_block_define():
    sudoku_matrix = [
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [1, 1, 1, 2, 2, 2, 3, 3, 3],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [4, 4, 4, 5, 5, 5, 6, 6, 6],
        [7, 7, 7, 8, 8, 8, 9, 9, 9],
        [7, 7, 7, 8, 8, 8, 9, 9, 9],
        [7, 7, 7, 8, 8, 8, 9, 9, 9]
    ]
    res_create = create_matrix(9,struct_case)
    block_define(res_create)
    for i in range(9):
        for j in range(9):
            assert sudoku_matrix[i][j] == res_create[i][j]['nblock']


def test_box_fill():
    test_matrix = create_matrix(9 , struct_case)
    x = 3
    y = 4
    valeur = 7
    box_fill(test_matrix, x, y, valeur)
    assert test_matrix[x][y]["val"] == valeur


def test_box_empty():
    test_matrix = create_matrix(9 , struct_case)
    x = 3
    y = 4
    set_val(test_matrix, x, y, 7)
    box_empty(test_matrix, x, y)
    assert test_matrix[x][y]["val"] == 0

def test_box_isempty():
    struct_case1 = {"nblock": 0, "Note_list": create_noteslist(), "val": 0} #struture pour matrice1
    struct_case2 = {"nblock": 0, "Note_list": create_noteslist(), "val": 1} #struture pour matrice2
    taille = 3  # exemple sur une matrice 3x3
    matrix1 = create_matrix(taille,struct_case1)          #création de la matrice1
    matrix2 = create_matrix(taille, struct_case2)         #création de la matrice2
    assert box_isempty(matrix1,1,1) == True         #test sur une case vide
    assert box_isempty(matrix2,2,2) == False        #test sur une case non-vide

  

def test_line_validation():
   
    valid_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],                # Créez une matrice Sudoku valide
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    for i in range(9):                                         # Testez des lignes valides
        assert line_validation(valid_sudoku, i) == True 

    
    invalid_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],                             # Testez une ligne invalide (doublon de 6)
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 6]  
    ]

    assert line_validation(invalid_sudoku, 8) == False  # Neuvième ligne invalide



def test_colon_validation():
    # Créez une matrice Sudoku valide
    valid_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

                                                           # Testez des colonnes valides
    for i in range(9):
        assert colon_validation(valid_sudoku, i) == True  # Colonnes valides

    
    invalid_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],                             # Testez une colonne invalide (doublon de 6)
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 6]  
    ]

    assert colon_validation(invalid_sudoku, 8) == False  # Neuvième colonne invalide
    



def test_block_members_validation ():
    # Créez une matrice Sudoku valide
    struct_case = {"nblock": 0, "Note_list": create_noteslist(), "val": 0}
    
    matrix_valide = create_matrix(9, struct_case)
    valid_sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    for i in range(9):
        for j in range(9):
            set_val(matrix_valide,i,j,valid_sudoku[i][j])
    

    for i in range(9):
        assert block_members_validation(matrix_valide, i+1) == True
    matrix_invalide = create_matrix(9, struct_case)    
    invalid_sudoku = [
        [5, 1, 4, 6, 7, 8, 9, 9, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 4, 4, 2, 5, 6, 7],
        [8, 8, 9, 7, 7, 1, 1, 2, 3],                             # Testez une colonne invalide (doublon de 6)
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [6, 6, 1, 3, 3, 7, 8, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 6]  
    ]
    for i in range(9):
        for j in range(9):
            set_val(matrix_invalide,i,j,invalid_sudoku[i][j])    
    for i in range(9):
        assert block_members_validation(matrix_invalide, i+1) == False


 







if __name__ == '__main__':
    test_create_matrix() 
    print("La fonction create_matrix a passé les tests avec succès.")

    test_create_noteList()
    print("La fonction test_create_noteList a passé les tests avec succès.")

    test_block_define()
    print("La fonction test_block_define() a passé les tests avec succès.")

    test_box_fill()
    print("La fonction test_box_fill() a passé les tests avec succès.")

    test_box_isempty()
    print("La fonction test_box_isempty a passé les tests avec succès.")

    test_box_empty()
    print("La fonction test_box_empty a passé les tests avec succès.")

    test_block_members_validation()
    print("la fonction test_block_validation a passé les tests avec succés")

