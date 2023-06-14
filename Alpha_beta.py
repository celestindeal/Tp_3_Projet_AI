
from Grid import Grid
from Jeton import Jeton
from Eval import evaluation
import math

jetonR = Jeton(Jeton.ROUGE)
jetonJ = Jeton(Jeton.JAUNE)

def Alpha_beta(profondeur, grid:Grid) :
    eval, action = JoueurMax(grid, profondeur,-math.inf,math.inf, Jeton.ROUGE)
    print(eval, "|", action)
    return action


# JoueurMax sera le joueur Rouge

def JoueurMax(n: Grid, p, alpha,beta, couleur: int):
    if n.isFeuille() or p == 0:
        bleh = n.eval(couleur)
        #print(">", bleh)
        return bleh, None
        #return evaluation(n,jetonR.couleur), None
    u = -math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonR)
        eval, _ = JoueurMin(n, p - 1,alpha,beta, couleur)
        n.remove_token(i)
        if eval > u:
            #print(eval, p)
            u = eval
            a = i           #af = i car c'est l'action à faire
        if u >= beta :
            return u, a
        alpha = max(alpha,u)

    return u, a

# JoueurMin sera le joueur Jaune
def JoueurMin(n:Grid, p,alpha,beta, couleur: int):
    if n.isFeuille() or p == 0:
        bleh = n.eval(couleur)
        #print("<", bleh)
        return bleh, None
        #return evaluation(n,jetonJ.couleur), None
    u = math.inf
    a = None
    for i in n.colonnePossible():
        n.play(i, jetonJ)
        eval, _ = JoueurMax(n, p - 1,alpha,beta, couleur)
        n.remove_token(i)
        if eval < u:
            #print(eval, p)
            u = eval
            a = i           #af = i car c'est l'action à faire
        if u <= beta :
            return u, a
        beta = min(beta,u)
            
    return u, a