
tableau = [[ 1,  2,  3,  4,  5,  6,  7],
           [ 8,  9, 10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19, 20, 21],
           [22, 23, 24, 25, 26, 27, 28],
           [29, 30, 31, 32, 33, 34, 35],
           [36, 37, 38, 39, 40, 41, 42],
           ]


def parcours_diagonal(tableau):
    rows = len(tableau)
    cols = len(tableau[0])

    # Parcours des diagonales supérieures
    for k in range(rows):
        i = k
        j = 0
        while i >= 0 and j < cols:
            print(tableau[i][j])
            i -= 1
            j += 1
        print('---')

    # Parcours des diagonales inférieures
    for k in range(1, cols):
        i = rows - 1
        j = k
        while i >= 0 and j < cols:
            print(tableau[i][j])
            i -= 1
            j += 1
        print("===")


parcours_diagonal(tableau)


def parcours_diagonale_descendante(tableau):
    rows = len(tableau)
    cols = len(tableau[0])

    diagonale = []
    
    # Parcours des diagonales descendantes supérieures
    for k in range(rows):
        i = k
        j = cols - 1
        while i >= 0 and j >= 0:
            diagonale.append(tableau[i][j])
            i -= 1
            j -= 1
    
    # Parcours des diagonales descendantes inférieures
    for k in range(1, cols):
        i = rows - 1
        j = k - 1
        while i >= 0 and j >= 0:
            diagonale.append(tableau[i][j])
            i -= 1
            j -= 1

    print(diagonale)

# Exemple d'utilisation

parcours_diagonale_descendante(tableau)

