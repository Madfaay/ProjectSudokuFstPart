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

