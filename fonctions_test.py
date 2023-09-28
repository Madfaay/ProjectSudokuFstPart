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

if __name__ == '__main__':
    test_create_matrix()
    print("La fonction create_matrix a passé les tests avec succès.")
