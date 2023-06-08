import numpy as np
from Jeton import Jeton

class Grid:


    def __init__(self):

        self.grid = np.zeros((6, 7))


    def getGrid(self):
        return self.grid
    
    def play(self, column, jeton):
        for i in range(5, -1, -1):
            if self.grid[i][column] == Jeton.VIDE:
                self.grid[i][column] = jeton.couleur
                print("Jeton joué en colonne " + str(column) + " et en ligne " + str(i))
                return True
        return False
        


    def toString(self) -> str:
        ()
        text = ""
        for i in self.grid:
            for j in i:
                if j == Jeton.JAUNE:
                    text += "O"
                elif j == Jeton.ROUGE:
                    text += "X"
                elif j == Jeton.VIDE:
                    text += "#"
            text += "\n"
        return text
    
    def colonnePossible(self):
        liste = []
        for i in range(6):
            if self.grid[0][i] == Jeton.VIDE:
                liste.append(i)
        return liste
    
    def isFeuille(self):
        return len(self.colonnePossible) == 0

    def eval(self, couleur :int):
        # Vérification des lignes
        for i in range(6):
            for j in range(4):
                if self.grid[i][j] == couleur and self.grid[i][j+1] == couleur and self.grid[i][j+2] == couleur and self.grid[i][j+3] == couleur:
                    return True

        # Vérification des colonnes
        for i in range(3):
            for j in range(7):
                if self.grid[i][j] == couleur and self.grid[i+1][j] == couleur and self.grid[i+2][j] == couleur and self.grid[i+3][j] == couleur:
                    return True

        # Vérification des diagonales ascendantes
        for i in range(3):
            for j in range(4):
                if self.grid[i][j] == couleur and self.grid[i+1][j+1] == couleur and self.grid[i+2][j+2] == couleur and self.grid[i+3][j+3] == couleur:
                    return True

        # Vérification des diagonales descendantes
        for i in range(3, 6):
            for j in range(4):
                if self.grid[i][j] == couleur and self.grid[i-1][j+1] == couleur and self.grid[i-2][j+2] == couleur and self.grid[i-3][j+3] == couleur:
                    return True

        return False
    

                    