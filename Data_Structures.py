
Matrix_length = 0


def create_matrix(taille):
    current_length = 0
    matrix = []
    liste_vide = []
    while current_length < taille:
        matrix.append(liste_vide)
        current_length += 1
        print(matrix)
    current_length = 0
    for grille in matrix:
        while current_length < taille:
            grille.append(0)
            current_length += 1
    current_length = 0
    return matrix


game_matrix = create_matrix(9)

print(game_matrix)
