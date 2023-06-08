from Grid import Grid
from Jeton import Jeton


# la colonne est un entier entre 0 et 6
# la ligne est un entier entre 0 et 5
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
grid.play(3, joueurJaune)
print(grid.toString())