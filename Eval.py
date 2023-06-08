

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
    for i in range(3):
        for j in range(6):
            if grid.grid[i][j] == couleurValide and grid.grid[i+1][j] == couleurValide and grid.grid[i+2][j] == couleurValide and grid.grid[i+3][j] == couleurValide:
                nbpoint += 100
            elif grid.grid[i][j] == couleurValide and grid.grid[i+1][j] == couleurValide and grid.grid[i+2][j] == couleurValide:
                nbpoint += 10
            elif grid.grid[i][j] == couleurValide and grid.grid[i+1][j] == couleurValide:
                nbpoint += 1

            if grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j] == couleurAdverse and grid.grid[i+2][j] == couleurAdverse and grid.grid[i+3][j] == couleurAdverse:
                nbpoint -= 100
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j] == couleurAdverse and grid.grid[i+2][j] == couleurAdverse:
                nbpoint -= 10
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j] == couleurAdverse:
                nbpoint -= 1

    # Vérification des diagonales ascendantes
    for i in range(3):
        for j in range(4):
            if grid.grid[i][j] == couleurValide and grid.grid[i+1][j+1] == couleurValide and grid.grid[i+2][j+2] == couleurValide and grid.grid[i+3][j+3] == couleurValide:
                nbpoint += 100
            elif grid.grid[i][j] == couleurValide and grid.grid[i+1][j+1] == couleurValide and grid.grid[i+2][j+2] == couleurValide:
                nbpoint += 10
            elif grid.grid[i][j] == couleurValide and grid.grid[i+1][j+1] == couleurValide:
                nbpoint += 1

            if grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j+1] == couleurAdverse and grid.grid[i+2][j+2] == couleurAdverse and grid.grid[i+3][j+3] == couleurAdverse:
                nbpoint -= 100
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j+1] == couleurAdverse and grid.grid[i+2][j+2] == couleurAdverse:
                nbpoint -= 10
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i+1][j+1] == couleurAdverse:
                nbpoint -= 1


    # Vérification des diagonales descendantes
    for i in range(3, 6):
        for j in range(4):
            if grid.grid[i][j] == couleurValide and grid.grid[i-1][j+1] == couleurValide and grid.grid[i-couleurAdverse][j+2] == couleurValide and grid.grid[i-3][j+3] == couleurValide:
                nbpoint += 100
            elif grid.grid[i][j] == couleurValide and grid.grid[i-1][j+1] == couleurValide and grid.grid[i-couleurAdverse][j+2] == couleurValide:
                nbpoint += 10
            elif grid.grid[i][j] == couleurValide and grid.grid[i-1][j+1] == couleurValide:
                nbpoint += 1

            if grid.grid[i][j] == couleurAdverse and grid.grid[i-1][j+1] == couleurAdverse and grid.grid[i-couleurAdverse][j+2] == couleurAdverse and grid.grid[i-3][j+3] == couleurAdverse:
                nbpoint -= 100
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i-1][j+1] == couleurAdverse and grid.grid[i-couleurAdverse][j+2] == couleurAdverse:
                nbpoint -= 10
            elif grid.grid[i][j] == couleurAdverse and grid.grid[i-1][j+1] == couleurAdverse:
                nbpoint -= 1

    return nbpoint