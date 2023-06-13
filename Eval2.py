from Jeton import Jeton


class Eval2:
    
    def __init__(self, grid):
        self.grid = grid
        self.total = 0
        self.count = 0
        self.countVide = 0

    def reset(self):
        self.count = 0
        self.countVide = 0

    def eval1(self, couleur :int):

        # Vérification des lignes
        print("ligne")
        for i in range(6):
            for j in range(5):
                self.eval_count(i, j, couleur, 6, 5)
            self.reset()

        self.reset()

        # Vérification des colonnes
        print("col")
        for i in range(6):
            for j in range(7):
                self.eval_count(i, j, couleur, 5, 6)
            self.reset()
                
        self.reset()
        print("da")
        self.parcours_diagonales_ascendantes(i, j, couleur)
        self.reset()
        print("dd")
        self.parcours_diagonales_descendantes(i, j, couleur)

        return self.total
    
    def parcours_diagonales_ascendantes(self, i: int, j:int, couleur: int):
        rows = len(self.grid)
        cols = len(self.grid[0])

        # Parcours des diagonales supérieures
        for k in range(rows):
            i = k
            j = 0
            while i >= 0 and j < cols:
                self.eval_count(i, j, couleur, 0, cols-1)
                i -= 1
                j += 1
            self.reset()

        # Parcours des diagonales inférieures
        for k in range(1, cols):
            i = rows - 1
            j = k
            while i >= 0 and j < cols:
                self.eval_count(i, j, couleur, 0, cols-1)
                i -= 1
                j += 1
            self.reset()

    def parcours_diagonales_descendantes(self, i: int, j:int, couleur: int):
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        # Parcours des diagonales descendantes supérieures
        for k in range(rows):
            i = k
            j = cols - 1
            while i >= 0 and j >= 0:
                self.eval_count(i, j, couleur, 0, 0)
                i -= 1
                j -= 1
            self.reset()
        
        # Parcours des diagonales descendantes inférieures
        for k in range(1, cols):
            i = rows - 1
            j = k - 1
            while i >= 0 and j >= 0:
                self.eval_count(i, j, couleur, 0, 0)
                i -= 1
                j -= 1
            self.reset()

    
    def eval_count(self, i: int, j:int, couleur: int, iEnd: int, jEnd: int):
        if self.grid[i][j] == couleur:
            self.count += 1
        elif self.grid[i][j] == Jeton.VIDE: 
            self.countVide += 1
        else:
            self.get_total(i, j)
            self.reset()
            return

        if i == iEnd or j == jEnd:
            self.get_total(i, j)
            self.reset()

    
    def get_total(self, i, j) -> int:
        if self.count == 1 and self.countVide >= 3:
            print(1, i, j)
            self.total += 1
        if self.count == 2 and self.countVide >= 2:
            print(5, i, j)
            self.total += 5
        if self.count == 3 and self.countVide >= 1:
            print(50, i, j)
            self.total += 50
        if self.count == 4:
            print(1000, i, j)
            self.total += 1000
        