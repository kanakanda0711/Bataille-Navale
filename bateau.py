class Bateau: 


    def __init__(self, ligne, colonne, longueur = 1, vertical = False, marque = '⛵'):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque
        self.position = []


    def positions(self):
        for l in range(self.longueur):
            if self.vertical == False: 
                self.position.append((self.ligne, self.colonne+l))
            else: 
                self.position.append((self.ligne+l, self.colonne))
        return self.position


    def coulé(self, grille):
        return all(
            grille.matrice[p[0]*grille.colonnes + p[1]] != '.'
            for p in self.position
        )           


class PorteAvion(Bateau):

    def __init__(self, ligne, colonne, longueur = 4, vertical = False, marque = '🚢'):
            super().__init__(ligne, colonne)
            self.longueur = longueur 
            self.vertical = vertical
            self.marque = marque
            self.position = []


class Croiseur(Bateau):

    def __init__(self, ligne, colonne, longueur = 3, vertical = False, marque = '⛴'):
            super().__init__(ligne, colonne)
            self.longueur = longueur 
            self.vertical = vertical
            self.marque = marque
            self.position = []


class Torpiller(Bateau):

    def __init__(self, ligne, colonne, longueur = 2, vertical = False, marque = '🚣'):
            super().__init__(ligne, colonne)
            self.longueur = longueur 
            self.vertical = vertical
            self.marque = marque
            self.position = []


class SousMarin(Bateau):

    def __init__(self, ligne, colonne, longueur = 2, vertical = False, marque = '🐟'):
            super().__init__(ligne, colonne)
            self.longueur = longueur 
            self.vertical = vertical
            self.marque = marque
            self.position = []

    