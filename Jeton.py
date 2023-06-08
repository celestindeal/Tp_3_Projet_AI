

class Jeton :
    """Classe représentant un jeton"""
    couleur = None  # Couleur du jeton (rouge ou jaune ou vide)
    JAUNE = 1
    ROUGE = 2
    VIDE = 0

    def __init__(self, couleur):
        """Constructeur de la classe"""
        self.couleur = couleur

    def getCouleur(self):
        """Méthode qui retourne la couleur du jeton"""
        return self.couleur

    def setCouleur(self, couleur):
        """Méthode qui modifie la couleur du jeton"""
        self.couleur = couleur
