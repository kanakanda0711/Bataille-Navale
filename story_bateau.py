from bateau import Bateau


'''Nom : "chevauchement"
Utilisateur : un joueur
Story : Positionner des bateaux sans chevauchement'''

'''chevauchement'''
b1 = Bateau(2,3,longueur=3)
print(b1.positions())
b2 = Bateau(2,3,longueur=3, vertical=True)
print(b2.positions())



