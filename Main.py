from Grid import Grid
from Jeton import Jeton
from Eval import eval_grid
from MinMax import MinMax

# la colonne est un entier entre 0 et 6
# la ligne est un entier entre 0 et 5 ; 5 est la ligne du bas; 0 est la ligne du haut
# pour la grid[ligne][colonne]




def Soleveur_puissanse_quatre (Grid :Grid, couleur :int) :  # A faire
    
    # Vérification des lignes
    for i in range(6):
        for j in range(4):
            if Grid[i][j] == couleur and Grid[i][j+1] == couleur and Grid[i][j+2] == couleur and Grid[i][j+3] == couleur:
                return True

      # Vérification des colonnes
    for i in range(3):
        for j in range(7):
            if Grid[i][j] == couleur and Grid[i+1][j] == couleur and Grid[i+2][j] == couleur and Grid[i+3][j] == couleur:
                return True

    # Vérification des diagonales ascendantes
    for i in range(3):
        for j in range(4):
            if Grid[i][j] == couleur and Grid[i+1][j+1] == couleur and Grid[i+2][j+2] == couleur and Grid[i+3][j+3] == couleur:
                return True

    # Vérification des diagonales descendantes
    for i in range(3, 6):
        for j in range(4):
            if Grid[i][j] == couleur and Grid[i-1][j+1] == couleur and Grid[i-2][j+2] == couleur and Grid[i-3][j+3] == couleur:
                return True

    return False
    


grid = Grid()
joueurJaune = Jeton(Jeton.JAUNE)
joueurRouge = Jeton(Jeton.ROUGE)
grid.play(0, joueurRouge)
grid.play(0, joueurRouge)
grid.play(0, joueurJaune)
grid.play(0, joueurRouge)

grid.play(1, joueurJaune)
grid.play(1, joueurJaune)
grid.play(1, joueurRouge)
grid.play(1, joueurJaune)
grid.play(1, joueurRouge)

grid.play(2, joueurJaune)
grid.play(2, joueurJaune)
grid.play(2, joueurRouge)
grid.play(2, joueurJaune)

grid.play(3, joueurRouge)
grid.play(3, joueurRouge)
grid.play(3, joueurJaune)

grid.play(4, joueurJaune)
grid.play(4, joueurRouge)
grid.play(4, joueurJaune)

grid.play(5, joueurJaune)
grid.play(5, joueurJaune)
grid.play(5, joueurJaune)
grid.play(5, joueurRouge)
grid.play(5, joueurRouge)
grid.play(5, joueurRouge)

grid.play(6, joueurRouge)
grid.play(6, joueurRouge)
grid.play(6, joueurRouge)
grid.play(6, joueurJaune)
grid.play(6, joueurJaune)
grid.play(6, joueurJaune)


print(grid.toString())
print(eval_grid(grid, Jeton.JAUNE, Jeton.ROUGE))
print(MinMax(3,grid))
print(grid.toString())