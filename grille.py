import sys

from termcolor import cprint

class Grille(): 

    vide = '.'

    def __init__(self, lignes, colonnes): 
        global vide 
        self.lignes = lignes
        self.colonnes = colonnes
        self.matrice = []
        self.bateau = []
        self.bateau_coulé = []
        for l in range(self.lignes):
            for c in range(self.colonnes):
                self.matrice.append(self.vide)

                
    def afficher(self):
        print(self)     


    def tirer(self,x,y):
       self.matrice[x*self.colonnes + y] = 'x'
       for b in self.bateau:
           if b.coulé(self) == True:
            self.bateau.remove(b)
            self.bateau_coulé.append(b)
            cprint(f"{b.__class__.__name__} coulé !", "red", attrs=["bold"], file=sys.stderr)
            print()
        

    def __str__(self):
        for b in self.bateau:
            position = b.positions()
            for p in position: 
                if self.matrice[p[0]*self.colonnes + p[1]] != self.vide: 
                    self.matrice[p[0]*self.colonnes + p[1]] = '💣'
        for b in self.bateau_coulé:
            position = b.positions()
            for p in position: 
                self.matrice[p[0]*self.colonnes + p[1]] = b.marque

        return "\n".join(
            "".join(self.matrice[c : c + self.colonnes])
            for c in range (0, len(self.matrice), self.colonnes)
        )


    def ajoute(self, bateau):
        position = bateau.positions()
        if position[bateau.longueur-1][0] <self.lignes and position[bateau.longueur-1][1] < self.colonnes:
            self.bateau.append(bateau)

            



        