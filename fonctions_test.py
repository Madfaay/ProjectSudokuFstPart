from Data_Structures import *

def test_create_matrix():
    # Créer une structure de test
    struct_case = {"nblock": 0, "Note_list": create_noteslist(), "val": 0}
    # Appeler la fonction create_matrix avec une taille de test
    taille = 3  # Par exemple, une matrice 3x3
    matrix = create_matrix(taille, struct_case)
    # Vérifier si la matrice a la bonne taille
    assert len(matrix) == taille
    for row in matrix:
        assert len(row) == taille
        # Vérifier si chaque élément de la matrice est une copie de la structure
        for element in row:
            assert element == struct_case

def test_box_isempty():
    struct_case1 = {"nblock": 0, "Note_list": create_noteslist(), "val": 0} #struture pour matrice1
    struct_case2 = {"nblock": 0, "Note_list": create_noteslist(), "val": 1} #struture pour matrice2
    taille = 3  # exemple sur une matrice 3x3
    matrix1 = create_matrix(taille,struct_case1)          #création de la matrice1
    matrix2 = create_matrix(taille, struct_case2)         #création de la matrice2
    assert box_isempty(matrix1,1,1) == True         #test sur une case vide
    assert box_isempty(matrix2,2,2) == False        #test sur une case non-vide

def test_box_empty():
    struct_case1 = {"nblock": 0, "Note_list": create_noteslist(), "val": 0} #struture pour matrice1
    struct_case2 = {"nblock": 0, "Note_list": create_noteslist(), "val": 1} #struture pour matrice2
    taille = 3 # test sur matrice 3x3
    matrix1 = create_matrix(taille, struct_case1)  # matrice final voulu
    matrix2 = create_matrix(taille, struct_case2)  # matrice de test
    for i in range(taille):
        for j in range(taille):
            matrix2=box_empty(matrix2, i, j)
            matrix2=box_empty(matrix2, i, j)
    assert matrix2 == matrix1  # compare les deux matrices


if __name__ == '__main__':
    test_create_matrix()
    print("La fonction create_matrix a passé les tests avec succès.")
    test_box_empty()
    print("La fonction test_box_empty a passé les tests avec succès.")
    test_box_isempty()
    print("La fonction test_box_isempty a passé les tests avec succès.")