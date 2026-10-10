from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpiller, SousMarin

'''Nom : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire'''


#créer une grille à 5 lignes et 8 colonnes
grille = Grille(5, 8)


for i in range(3):
    #afficher la grille à l'écran
    print(grille) 
    #demande à l'utilisateur de rentrer deux coordonnées x et y
    x = int(input (" Coordonnee x "))
    y = int(input (" Corrdonnee y "))
    #tier à l'endroit indiqué sur la grille
    grille.tirer(x, y)
    #retour en 2
print(grille)


grille.ajoute(Bateau(1, 0, longueur=2))
grille.ajoute(PorteAvion(2, 0, vertical = False))
print(grille)
