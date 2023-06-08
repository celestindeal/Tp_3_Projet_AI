
from Grid import Grid
from Jeton import Jeton
from Joueur import Joueur
import math


def MinMax(profondeur, grid:Grid) :
    eval, action = JoueurMax(grid, profondeur)
    return action


# JoueurMax sera le joueur Rougee

def JoueurMax(n: Grid, p):
    if n.isFeuille() or p == 0:
        return n.eval(Jeton.ROUGE), None
    u = -math.inf
    a = None
    for i in n.colonnePossible():
        f = n.play(i, Joueur.Rouge)
        eval, _ = JoueurMin(n, p - 1)
        if eval > u:
            u = eval
            a = i           #af = i car c'est l'action à faire

    return u, a

# JoueurMin sera le joueur Jaune
def JoueurMin(n:Grid, p):
    if n.isFeuille() or p == 0:
        return n.eval(Jeton.JAUNE), None
    u = math.inf
    a = None
    for i in n.colonnePossible():
        f = n.play(i, Joueur.Jaune)
        eval, _ = JoueurMax(n, p - 1)
        if eval < u:
            u = eval
            a = i           #af = i car c'est l'action à faire
            
    return u, a