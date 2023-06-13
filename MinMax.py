
from Grid import Grid
from Jeton import Jeton
from Eval import eval_grid
import math

jetonR = Jeton(Jeton.ROUGE)
jetonJ = Jeton(Jeton.JAUNE)

def MinMax(profondeur, grid:Grid, nextJ: Jeton) :
    eval, action = JoueurMax(grid, profondeur, nextJ)
    print(eval)
    return action


# JoueurMax sera le joueur Rougee

def JoueurMax(n: Grid, p, joueur: Jeton):
    if n.isFeuille() or p == 0:
        return n.eval(joueur), None
        #return eval_grid(n,jetonR.couleur,jetonJ.couleur), None
    u = -math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, joueur)
        joueur.inverserCouleur()
        eval, _ = JoueurMin(n, p - 1, joueur)
        n.remove_token(i)
        if eval > u:
            u = eval
            a = i           #af = i car c'est l'action à faire

    return u, a

# JoueurMin sera le joueur Jaune
def JoueurMin(n:Grid, p, joueur: Jeton):
    if n.isFeuille() or p == 0:
        return n.eval(joueur), None
        #return eval_grid(n,jetonJ.couleur,jetonR.couleur), None
    u = math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, joueur)
        joueur.inverserCouleur()
        eval, _ = JoueurMax(n, p - 1, joueur)
        n.remove_token(i)
        if eval < u:
            u = eval
            a = i           #af = i car c'est l'action à faire
            
    return u, a