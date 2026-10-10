from termcolor import colored

from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpiller, SousMarin

'''Nom : "Bataille Navale"
Utilisateur : un joueur
Developpeur : Kana KANDA
Story : On veut pouvoir gérer les tirs de l'adversaire'''


#créer une grille à 5 lignes et 8 colonnes
grille = Grille(8, 10)


grille.ajoute(PorteAvion(2, 0, vertical = True))
grille.ajoute(Croiseur(3, 3))
grille.ajoute(Torpiller(5, 4))
grille.ajoute(SousMarin(6, 2))

i = 0 

while grille.bateau != []:
    #afficher la grille à l'écran
    
    print(" ")
    #demande à l'utilisateur de rentrer deux coordonnées x et y
    x = int(input (" Coordonnee x "))
    y = int(input (" Corrdonnee y "))
    #tier à l'endroit indiqué sur la grille
    grille.tirer(x, y)
    grille.afficher()
    #retour en 2
    i +=1


print(" ")
grille.afficher()

text = colored("Bataille Navale completé, il vous a fallu " f"{i} étapes!", "red", attrs=["reverse", "blink"])
print(text)




