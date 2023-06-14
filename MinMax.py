
from Grid import Grid
from Jeton import Jeton
from Eval import evaluation
import math

jetonR = Jeton(Jeton.ROUGE)
jetonJ = Jeton(Jeton.JAUNE)

def MinMax(profondeur, grid:Grid) :
    eval, action = JoueurMax(grid, profondeur, Jeton.ROUGE)
    print(eval, "|", action)
    return action


# JoueurMax sera le joueur Rouge

def JoueurMax(n: Grid, p, couleur: int):
    if n.isFeuille() or p == 0:
        bleh = n.eval(couleur)
        #print(">", bleh)
        return bleh, None
        #return evaluation(n,jetonR.couleur), None
    u = -math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonR)
        eval, _ = JoueurMin(n, p - 1, couleur)
        n.remove_token(i)
        if eval > u:
            #print(eval, p)
            u = eval
            a = i           #af = i car c'est l'action à faire

    return u, a

# JoueurMin sera le joueur Jaune
def JoueurMin(n:Grid, p, couleur):
    if n.isFeuille() or p == 0:
        bleh = n.eval(couleur)
        #print("<", bleh)
        return bleh, None
        #return evaluation(n,jetonJ.couleur), None
    u = math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonJ)
        eval, _ = JoueurMax(n, p - 1, couleur)
        n.remove_token(i)
        if eval < u:
            #print(eval, p)
            u = eval
            a = i           #af = i car c'est l'action à faire
            
    return u, a