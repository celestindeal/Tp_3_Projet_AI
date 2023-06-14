from Grid import Grid
from Jeton import Jeton
from Eval import eval_grid
from MinMax import MinMax

# la colonne est un entier entre 0 et 6
# la ligne est un entier entre 0 et 5 ; 5 est la ligne du bas; 0 est la ligne du haut
# pour la grid[ligne][colonne]








def jouer(grid: Grid, moi : Jeton, adversaire : Jeton, profondeur : int) :
    while not grid.isFeuille() and not grid.Soleveur_puissanse_quatre(moi.couleur) and not grid.Soleveur_puissanse_quatre(adversaire.couleur):
        valeur = MinMax(profondeur, grid)
        grid.play(valeur, adversaire)
        print(grid.toString())
        
        valeur = input("Veuillez entrer une valeur : ")
        grid.play(int(valeur)- 1, moi)

    if grid.Soleveur_puissanse_quatre(moi.couleur):
        print("J'ai gagné !")
    elif grid.Soleveur_puissanse_quatre(adversaire.couleur):
        print("J'ai perdu !")
    



grid = Grid()
joueurJaune = Jeton(Jeton.JAUNE)
joueurRouge = Jeton(Jeton.ROUGE)
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

jouer(grid, joueurJaune, joueurRouge, 4)






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
