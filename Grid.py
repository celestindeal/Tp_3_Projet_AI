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
                return True
        return False
    
    def remove_token(self, column):
        for i in range(6):
            if self.grid[i][column] != Jeton.VIDE:
                self.grid[i][column] = Jeton.VIDE
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
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 6, 5)

        count = 0
        countVide = 0

        # Vérification des colonnes
        for i in range(5):
            for j in range(6):
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 5, 6)
                
        count = 0
        countVide = 0
        _, _, total = self.parcours_diagonales_ascendantes(i, j, couleur, count, countVide, total)
        count = 0
        countVide = 0
        _, _, total = self.parcours_diagonales_descendantes(i, j, couleur, count, countVide, total)

        return total
    
    def parcours_diagonales_ascendantes(self, i: int, j:int, couleur: int, count: int, countVide: int, total: int) -> (int, int, int):
        rows = len(self.grid)
        cols = len(self.grid[0])

        # Parcours des diagonales supérieures
        for k in range(rows):
            i = k
            j = 0
            while i >= 0 and j < cols:
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 0, cols-1)
                i -= 1
                j += 1
            count = 0
            countVide = 0

        # Parcours des diagonales inférieures
        for k in range(1, cols):
            i = rows - 1
            j = k
            while i >= 0 and j < cols:
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 0, cols-1)
                i -= 1
                j += 1
            count = 0
            countVide = 0
        return (count, countVide, total)

    def parcours_diagonales_descendantes(self, i: int, j:int, couleur: int, count: int, countVide: int, total: int) -> (int, int, int):

        rows = len(self.grid)
        cols = len(self.grid[0])
        
        # Parcours des diagonales descendantes supérieures
        for k in range(rows):
            i = k
            j = cols - 1
            while i >= 0 and j >= 0:
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 0, 0)
                i -= 1
                j -= 1
            count = 0
            countVide = 0
        
        # Parcours des diagonales descendantes inférieures
        for k in range(1, cols):
            i = rows - 1
            j = k - 1
            while i >= 0 and j >= 0:
                count, countVide, total = self.eval_count(i, j, couleur, count, countVide, total, 0, 0)
                i -= 1
                j -= 1
            count = 0
            countVide = 0

        return (count, countVide, total)
    
    def eval_count(self, i: int, j:int, couleur: int, count: int, countVide: int, total: int,
                         iEnd: int, jEnd: int) -> (int, int, int):
        if self.grid[i][j] == couleur:
            count += 1
        elif self.grid[i][j] == Jeton.VIDE: 
            countVide += 1
            if i == iEnd or j == jEnd:
                total = self.get_total(count, countVide, total, i, j)
                count = 0
                countVide = 0
        else:
            total = self.get_total(count, countVide, total, i, j)
            count = 0
            countVide = 0

        return (count, countVide, total)
    
    def get_total(self, count, countVide, total, i, j) -> int:
        if count == 1 and countVide >= 3:
            total += 1
        if count == 2 and countVide >= 2:
            total += 5
        if count == 3 and countVide >= 1:
            total += 50
        if count == 4:
            total += 1000
        return total
        

                        