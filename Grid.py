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
    
    def remove_token(self, column):
        for i in range(6):
            if self.grid[i][column] != Jeton.VIDE:
                self.grid[i][column] = Jeton.VIDE
                print("Jeton supprimé de la colonne " + str(column) + " et de la ligne " + str(i))
                return True
        return False

        


    def toString(self) -> str:
        ()
        text = ""
        for i in self.grid:
            for j in i:
                if j == Jeton.JAUNE:
                    text += "O "
                elif j == Jeton.ROUGE:
                    text += "X "
                elif j == Jeton.VIDE:
                    text += "# "
            text += "\n"
        return text
    
    def colonnePossible(self):
        liste = []
        for i in range(6):
            if self.grid[0][i] == Jeton.VIDE:
                liste.append(i)
        print(liste)
        return liste
    
    def isFeuille(self):
        return len(self.colonnePossible()) == 0

    def eval1(self, couleur :int):
        total = 0
        count = 0
        countVide = 0

        # Vérification des lignes
        for i in range(6):
            for j in range(5):
                if self.grid[i][j] == couleur:
                    count += 1
                    countVide = 0
                elif self.grid[i][j] == Jeton.VIDE and j != 5:
                    countVide += 1
                else:
                    if count == 1 and countVide >= 3:
                        total += 1
                    if count == 2 and countVide >= 2:
                        total += 5
                    if count == 3 and countVide >= 1:
                        total += 50
                    if count == 4:
                        total += 1000
                    count = 0
                    countVide = 0


        # Vérification des colonnes
        for i in range(5):
            for j in range(6):
                if self.grid[i][j] == couleur:
                    count += 1
                    countVide = 0
                elif self.grid[i][j] == Jeton.VIDE and i != 6:
                    countVide += 1
                else:
                    if count == 1 and countVide >= 3:
                        total += 1
                    if count == 2 and countVide >= 2:
                        total += 5
                    if count == 3 and countVide >= 1:
                        total += 50
                    if count == 4:
                        total += 1000
                    count = 0
                    countVide = 0
                


        # Vérification des diagonales ascendantes
        for i in range(3):
            for j in range(4):
                if self.grid[i][j] == couleur:
                    return True

        # Vérification des diagonales descendantes
        for i in range(3, 6):
            for j in range(4):
                if self.grid[i][j] == couleur:
                    return True

        return False
    

                    