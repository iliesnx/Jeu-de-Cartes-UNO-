from carte import Carte
from paquet import Paquet

# --- Démonstration de la classe Carte ---
print("=== Classe Carte ===")
c1 = Carte(3, 'COEUR')
c2 = Carte('ROI', 'PIQUE')
print(f"{c1}  ->  {c1.points()} point(s)")
print(f"{c2}  ->  {c2.points()} point(s)")

try:
    Carte(15, 'COEUR')
except ValueError as e:
    print(f"ValueError : {e}")

# --- Démonstration de la classe Paquet ---
print("\n=== Classe Paquet ===")
p = Paquet()
print(p)

p.melanger()
print("Paquet mélangé.")

p.couper()
print("Paquet coupé.")

carte_piochee = p.piocher()
print(f"Carte piochée : {carte_piochee}  ({len(p)} cartes restantes)")

print("\nDistribution à 4 joueurs, 5 cartes chacun :")
mains = p.distribuer(joueurs=4, cartes=5)
for i, main in enumerate(mains):
    print(f"  Joueur {i + 1} : {main}")

print(f"\nCartes restantes dans le paquet : {len(p)}")
