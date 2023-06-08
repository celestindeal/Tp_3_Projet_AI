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
                    