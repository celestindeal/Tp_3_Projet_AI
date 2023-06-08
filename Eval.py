

from Grid import Grid


def eval_grid(grid : Grid, couleurValide : int, couleurAdverse : int):
    nbpoint = 0
    # Vérification des lignes
    for j in range(6):
        for i in range(4):
            compte = 0
            if grid.grid[i][j] == couleurValide and grid.grid[i][j+1] == couleurValide and grid.grid[i][j+2] == couleurValide and grid.grid[i][j+3] == couleurValide:
                nbpoint += 100
            elif grid.grid[i][j] == couleurValide and grid.grid[i][j+1] == couleurValide and grid.grid[i][j+2] == couleurValide:
                nbpoint += 10
            elif grid.grid[i][j] == couleurValide and grid.grid[i][j+1] == couleurValide:
                nbpoint += 1
            
            if grid.grid[i][j] == couleurAdverse and grid.grid[i][j+1] == couleurAdverse and grid.grid[i][j+2] == couleurAdverse and grid.grid[i][j+3] == couleurAdverse:
                nbpoint += 100
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i][j+1] == couleurAdverse and grid.grid[i][j+2] == couleurAdverse:
                nbpoint += 10
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i][j+1] == couleurAdverse:
                nbpoint += 1
                


    # Vérification des colonnes
    for j in range(3):
        for i in range(7):
            if grid.grid[i][j] == 1 and grid.grid[i+1][j] == 1 and grid.grid[i+2][j] == 1 and grid.grid[i+3][j] == 1:
                nbpoint += 100
            elif grid.grid[i][j] == 1 and grid.grid[i+1][j] == 1 and grid.grid[i+2][j] == 1:
                nbpoint += 10
            elif grid.grid[i][j] == 1 and grid.grid[i+1][j] == 1:
                nbpoint += 1

            if grid.grid[i][j] == 2 and grid.grid[i+1][j] == 2 and grid.grid[i+2][j] == 2 and grid.grid[i+3][j] == 2:
                nbpoint -= 100
            elif grid.grid[i][j] == 2 and grid.grid[i+1][j] == 2 and grid.grid[i+2][j] == 2:
                nbpoint -= 10
            elif grid.grid[i][j] == 2 and grid.grid[i+1][j] == 2:
                nbpoint -= 1

    # Vérification des diagonales ascendantes
    for j in range(3):
        for i in range(4):
            if grid.grid[i][j] == 1 and grid.grid[i+1][j+1] == 1 and grid.grid[i+2][j+2] == 1 and grid.grid[i+3][j+3] == 1:
                nbpoint += 100
            elif grid.grid[i][j] == 1 and grid.grid[i+1][j+1] == 1 and grid.grid[i+2][j+2] == 1:
                nbpoint += 10
            elif grid.grid[i][j] == 1 and grid.grid[i+1][j+1] == 1:
                nbpoint += 1

            if grid.grid[i][j] == 2 and grid.grid[i+1][j+1] == 2 and grid.grid[i+2][j+2] == 2 and grid.grid[i+3][j+3] == 2:
                nbpoint -= 100
            elif grid.grid[i][j] == 2 and grid.grid[i+1][j+1] == 2 and grid.grid[i+2][j+2] == 2:
                nbpoint -= 10
            elif grid.grid[i][j] == 2 and grid.grid[i+1][j+1] == 2:
                nbpoint -= 1


    # Vérification des diagonales descendantes
    for j in range(3, 6):
        for i in range(4):
            if grid.grid[i][j] == 1 and grid.grid[i-1][j+1] == 1 and grid.grid[i-2][j+2] == 1 and grid.grid[i-3][j+3] == 1:
                nbpoint += 100
            elif grid.grid[i][j] == 1 and grid.grid[i-1][j+1] == 1 and grid.grid[i-2][j+2] == 1:
                nbpoint += 10
            elif grid.grid[i][j] == 1 and grid.grid[i-1][j+1] == 1:
                nbpoint += 1

            if grid.grid[i][j] == 2 and grid.grid[i-1][j+1] == 2 and grid.grid[i-2][j+2] == 2 and grid.grid[i-3][j+3] == 2:
                nbpoint -= 100
            elif grid.grid[i][j] == 2 and grid.grid[i-1][j+1] == 2 and grid.grid[i-2][j+2] == 2:
                nbpoint -= 10
            elif grid.grid[i][j] == 2 and grid.grid[i-1][j+1] == 2:
                nbpoint -= 1

    return nbpoint