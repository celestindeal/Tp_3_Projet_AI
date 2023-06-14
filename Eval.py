

from Grid import Grid

def evaluation(grid : Grid, couleur : int):
    return eval_grid(grid, couleur) - eval_grid(grid, int(not bool(couleur - 1)) + 1)


def eval_grid(grid : Grid, couleur : int):
    nbpoint = 0
    # Vérification des lignes
    for j in range(6):
        for i in range(4):
            if grid.grid[i][j] == couleur and grid.grid[i][j+1] == couleur and grid.grid[i][j+2] == couleur and grid.grid[i][j+3] == couleur:
                nbpoint += 100
            elif grid.grid[i][j] == couleur and grid.grid[i][j+1] == couleur and grid.grid[i][j+2] == couleur:
                nbpoint += 10
            elif grid.grid[i][j] == couleur and grid.grid[i][j+1] == couleur:
                nbpoint += 1
                

    # Vérification des colonnes
    for i in range(3):
        for j in range(6):
            if grid.grid[i][j] == couleur and grid.grid[i+1][j] == couleur and grid.grid[i+2][j] == couleur and grid.grid[i+3][j] == couleur:
                nbpoint += 100
            elif grid.grid[i][j] == couleur and grid.grid[i+1][j] == couleur and grid.grid[i+2][j] == couleur:
                nbpoint += 10
            elif grid.grid[i][j] == couleur and grid.grid[i+1][j] == couleur:
                nbpoint += 1

    # Vérification des diagonales ascendantes
    for i in range(3):
        for j in range(4):
            if grid.grid[i][j] == couleur and grid.grid[i+1][j+1] == couleur and grid.grid[i+2][j+2] == couleur and grid.grid[i+3][j+3] == couleur:
                nbpoint += 100
            elif grid.grid[i][j] == couleur and grid.grid[i+1][j+1] == couleur and grid.grid[i+2][j+2] == couleur:
                nbpoint += 10
            elif grid.grid[i][j] == couleur and grid.grid[i+1][j+1] == couleur:
                nbpoint += 1


    # Vérification des diagonales descendantes
    for i in range(3, 6):
        for j in range(4):
            if grid.grid[i][j] == couleur and grid.grid[i-1][j+1] == couleur and grid.grid[i-2][j+2] == couleur and grid.grid[i-3][j+3] == couleur:
                nbpoint += 100
            elif grid.grid[i][j] == couleur and grid.grid[i-1][j+1] == couleur and grid.grid[i-2][j+2] == couleur:
                nbpoint += 10
            elif grid.grid[i][j] == couleur and grid.grid[i-1][j+1] == couleur:
                nbpoint += 1

    return nbpoint