from grille import Grille
from bateau import Bateau

def test_init():
    grille = Grille()
    assert isinstance(grille, Grille)

g1 = Grille(5, 8)

# for c in range (0, len(g.matrice), g.colonnes):
#     print(*g.matrice[c : c + g.colonnes])

g1.afficher()
print(" ")
# g1.tirer(2, 3)
# print(g1)
# print(" ")

g2 = Grille(2, 3)
g2.afficher()
print(" ")

g2.ajoute(Bateau(1, 0, longueur=2))
print(g2)

g2.ajoute(Bateau(1, 0, longueur=2, vertical = True))
g2.ajoute(Bateau(1, 0, longueur=4, vertical=True))
print(g2)









