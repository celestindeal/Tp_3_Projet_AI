from Jeton import Jeton
from Grid import Grid

class State():

    def __init__(self, couleur: Jeton, grid: Grid) -> None:
        self.couleur = couleur
        self.grid = grid



class Noeud():

    def __init__(self, Children: list, Parent, action: int, state: State) -> None:
        self.Children = Children
        self.Parent = Parent
        self.action = action
        self.state = state

        self.N = 0
        self.Q = 0

        self.triedActions = []
    
    def isFullExpanded(self):
        return len(self.state.grid.colonnePossible()) == len(self.triedActions)
    
