import copy
import math
import random
from neud import State, Noeud
from random import randint
from copy import deepcopy
from math import sqrt, log
from operator import itemgetter

Cp = 1.4

def UTCSearch(s0: State, nbIteration: int):
    v0: Noeud = Noeud([], None, None, s0)              # noeud prec
    iteration: int = 0
    while(iteration < nbIteration):
        v1: Noeud = TreePolicy(v0)                     # noeud suivant
        Delta = DefaultPolicy(v1.state)
        Backup(v1, Delta)

        iteration += 1
    return BestChild(v0, 0).action


def TreePolicy(v: Noeud) -> Noeud:
    global Cp
    while( not v.state.grid.isFeuille()):
        if not v.isFullExpanded():
            return Expand(v)
        else:
            v = BestChild(v, Cp)
    return v


def Expand(v: Noeud) -> Noeud:

    # choisir une action
    A:list[int] = v.state.grid.colonnePossible()
    a:int       = A[random.randint(0, len(A)-1)]
    v.triedActions.append(a)

    # créer le state du child
    s_prime: State = copy.deepcopy(v.state)
    s_prime.couleur.inverserCouleur()
    s_prime.grid.play(a, s_prime.couleur)

    v_prime: Noeud = Noeud([], v, a, s_prime)
    v.Children.append(v_prime)

    return v_prime


def  BestChild(v: Noeud, c: float):
    values = []
    for v_prime in v.Children:
        value = v_prime.Q / v_prime.N + c * math.sqrt((2 * math.log(v.N)) / v_prime.N)
        values.append((value, v_prime))
    
    if len(v.Children) == 0:
        return None
    if len(values) == 0:
        return 0
    return max(values, key=itemgetter(0))[1]

def DefaultPolicy(s: State) -> int:
    while(not s.grid.isFeuille()):
        s.couleur.inverserCouleur()
        values = s.grid.colonnePossible()
        s.grid.play(values[random.randint(0, len(values)-1)], s.couleur)
    if s.grid.eval(s.couleur.couleur) > 1000:
        return 1
    elif s.grid.eval(s.couleur.couleur) < -1000:
        return -1
    else:
        return 0
        

def Backup(v: Noeud, Delta: int):
    while v != None:
        v.N += 1
        v.Q += Delta
        Delta = - Delta
        v = v.Parent