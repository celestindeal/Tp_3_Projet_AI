import numpy as np
from Jeton import Jeton
from Eval2 import Eval2

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
        text = "O : Jaune\nX : Rouge\n\n"
        for i in self.grid:
            for j in i:
                if j == Jeton.JAUNE:
                    text += "O "
                elif j == Jeton.ROUGE:
                    text += "X "
                elif j == Jeton.VIDE:
                    text += ". "
            text += "\n"
        for i in range(1, 8, 1):
            text += str(i) + " "
        text+= "\n"
        return text
    
    def colonnePossible(self):
        liste = []
        for i in range(6):
            if self.grid[0][i] == Jeton.VIDE:
                liste.append(i)
        return liste
    
    def isFeuille(self):
        return len(self.colonnePossible()) == 0


    def eval(self, couleur :Jeton):
        
        eval = Eval2(self.grid)

        a = eval.eval1(couleur.couleur)
        #print('---')
        eval.total = 0
        couleur.inverserCouleur()
        b = eval.eval1(couleur.couleur)
        print(">>>", a)
        print(">>>", b)
        return a - b

                        