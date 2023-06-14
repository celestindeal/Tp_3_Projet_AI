import copy
from Alpha_beta import Alpha_beta
from Grid import Grid
from Jeton import Jeton
from Eval import eval_grid
from MinMax import MinMax
from MCTS import UTCSearch
from neud import State

# la colonne est un entier entre 0 et 6
# la ligne est un entier entre 0 et 5 ; 5 est la ligne du bas; 0 est la ligne du haut
# pour la grid[ligne][colonne]


def jouer_compte_ordi(Algo:int,grid: Grid, moi : Jeton, adversaire : Jeton, profondeur : int) :
    while not grid.isFeuille() and not grid.Soleveur_puissanse_quatre(moi.couleur) and not grid.Soleveur_puissanse_quatre(adversaire.couleur):
        valeur = 0
        if Algo == 0:
            valeur = MinMax(profondeur, grid)
        elif Algo == 1:
            valeur = Alpha_beta(profondeur, grid)
        else:
            state = State(adversaire, copy.deepcopy(grid))
            valeur = UTCSearch(state, int(profondeur))
        grid.play(valeur, adversaire)
        print(grid.toString())
        
        valeur = input("Veuillez entrer une valeur : ")
        grid.play(int(valeur)- 1, moi)
        print(grid.toString())

    if grid.Soleveur_puissanse_quatre(moi.couleur):
        print("J'ai gagné !")
    elif grid.Soleveur_puissanse_quatre(adversaire.couleur):
        print("J'ai perdu !")
    

def defi_ordi(Algo:int, profondeur : int ,Algo1:int, profondeur1 : int, couleur : Jeton, couleur1 : Jeton ,grid: Grid) :
    valeur = 0
    while not grid.isFeuille() and not grid.Soleveur_puissanse_quatre(couleur.couleur) and not grid.Soleveur_puissanse_quatre(couleur1.couleur):
       
        if Algo == 0:
            valeur = MinMax(profondeur, grid)
        elif Algo == 1:
            valeur = Alpha_beta(profondeur, grid)
        else:
            state = State(couleur, copy.deepcopy(grid))
            valeur = UTCSearch(state, int(profondeur))
        grid.play(valeur, couleur)
        print(grid.toString())
        
        if not grid.Soleveur_puissanse_quatre(couleur.couleur):
            if Algo1 == 0:
                valeur = MinMax(profondeur1, grid)
            elif Algo1 == 1:
                valeur = Alpha_beta(profondeur1, grid)
            else:
                state = State(couleur1, copy.deepcopy(grid))
                valeur = UTCSearch(state, int(profondeur1))
            grid.play(valeur, couleur1)
            print(grid.toString())
    
    if grid.Soleveur_puissanse_quatre(couleur.couleur):
        print("ALgo à gagné !")
    elif grid.Soleveur_puissanse_quatre(couleur1.couleur):
        print("ALgo1 à gagné !")
        
        






grid = Grid()
joueurJaune = Jeton(Jeton.JAUNE)
joueurRouge = Jeton(Jeton.ROUGE)


print( " O pour jouer contre l'ordinateur, \n 1 pour faire s'affronter les ordinateurs entre eux ")
valeur = input("Veuillez entrer une valeur : ")
if( int(valeur) ):
    print("Pour le premier joueur : \n 0 MinMax, \n 1 Alpha Beta \n 2 MCTS ")
    algo = input("Veuillez entrer une valeur : ")
    print("Choisis ton niveau ")
    niveau = input("Veuillez entrer une valeur : ")

    print("Pour le premier joueur : \n 0 MinMax, \n 1 Alpha Beta \n 2 MCTS ")
    algo1 = input("Veuillez entrer une valeur : ")
    print("Choisis ton niveau ")
    niveau1 = input("Veuillez entrer une valeur : ")

    defi_ordi(int(algo), int(niveau), int(algo1), int(niveau1), joueurJaune, joueurRouge, grid)
    
else :
    print( " 0 jouer contre MinMax, \n 1 jouer contre Alpha Beta \n 2 jouer contre MCTS ")
    algo = input("Veuillez entrer une valeur : ")
    algo = int(algo)
    if( algo == 0 ):
        print("Choisis ton niveau entre 1 et 8")
        niveau = input("Veuillez entrer une valeur : ")
        jouer_compte_ordi(algo,grid, joueurJaune, joueurRouge, int(niveau))
    elif( algo == 1 ):
        print("Choisis ton niveau entre 1 et 8")
        niveau = input("Veuillez entrer une valeur : ")
        jouer_compte_ordi(algo,grid, joueurJaune, joueurRouge, int(niveau))
    elif( algo == 2 ):
        print("Choisis ton niveau entre 1 et 100")
        niveau = input("Veuillez entrer une valeur : ")
        jouer_compte_ordi(algo,grid, joueurJaune, joueurRouge, int(niveau) * 100)




# tableau = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

# tableau2 = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 2, 1, 0, 0, 0],
#     [0, 0, 2, 2, 0, 0, 0],
#     [1, 1, 2, 2, 2, 0, 1]
# ]

# tableau3 = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [2, 0, 0, 0, 0, 0, 0],
#     [1, 1, 2, 2, 2, 1, 0],
#     [2, 2, 1, 1, 1, 2, 0],
#     [2, 2, 1, 2, 1, 1, 1]
# ]

# tableau4 = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0],
#     [2, 0, 1, 1, 1, 2, 0]
# ]

# tab3 ^
# . . . . . . .
# . . . . . . .
# X . . . X . .
# O O X X X O .
# X X O O O X .
# X X O X O O O



# grid.grid = tableau2
# print(grid.toString())
# #print(grid.eval(Jeton(Jeton.JAUNE)))
# print(grid.eval(Jeton(Jeton.ROUGE)))

# grid.play(0, joueurRouge)
# grid.play(0, joueurRouge)
# grid.play(0, joueurJaune)
# grid.play(0, joueurRouge)

# grid.play(1, joueurJaune)
# grid.play(1, joueurJaune)
# grid.play(1, joueurRouge)
# grid.play(1, joueurJaune)
# grid.play(1, joueurRouge)

# grid.play(2, joueurJaune)
# grid.play(2, joueurJaune)
# grid.play(2, joueurRouge)
# grid.play(2, joueurJaune)

# grid.play(3, joueurRouge)
# grid.play(3, joueurRouge)
# grid.play(3, joueurJaune)

# grid.play(4, joueurJaune)
# grid.play(4, joueurRouge)
# grid.play(4, joueurJaune)

# grid.play(5, joueurJaune)
# grid.play(5, joueurJaune)
# grid.play(5, joueurJaune)
# grid.play(5, joueurRouge)
# grid.play(5, joueurRouge)
# grid.play(5, joueurRouge)

# grid.play(6, joueurRouge)
# grid.play(6, joueurRouge)
# grid.play(6, joueurRouge)
# grid.play(6, joueurJaune)
# grid.play(6, joueurJaune)
# grid.play(6, joueurJaune)


# print(grid.toString())
# print(eval_grid(grid, Jeton.JAUNE, Jeton.ROUGE))
# print(MinMax(1,grid))
# print(grid.toString())