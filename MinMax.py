
from Grid import Grid
from Jeton import Jeton
from Eval import eval_grid
import math

jetonR = Jeton(Jeton.ROUGE)
jetonJ = Jeton(Jeton.JAUNE)

def MinMax(profondeur, grid:Grid) :
    eval, action = JoueurMax(grid, profondeur)
    return action


# JoueurMax sera le joueur Rougee

def JoueurMax(n: Grid, p):
    if n.isFeuille() or p == 0:
        return eval_grid(n,jetonR,jetonJ), None
    u = -math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonR)
        eval, _ = JoueurMin(n, p - 1)
        n.remove_token(i)
        if eval > u:
            u = eval
            a = i           #af = i car c'est l'action à faire

    return u, a

# JoueurMin sera le joueur Jaune
def JoueurMin(n:Grid, p):
    if n.isFeuille() or p == 0:
        return eval_grid(n,jetonJ,jetonR), None
    u = math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonJ)
        eval, _ = JoueurMax(n, p - 1)
        n.remove_token(i)
        if eval < u:
            u = eval
            a = i           #af = i car c'est l'action à faire
            
    return u, a