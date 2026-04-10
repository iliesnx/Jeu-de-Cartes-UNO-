import random
from carte import Carte, VALEURS_VALIDES, COULEURS_VALIDES


class Paquet:
    def __init__(self):
        self._cartes = [
            Carte(valeur, couleur)
            for couleur in COULEURS_VALIDES
            for valeur in VALEURS_VALIDES
        ]

    def __len__(self):
        return len(self._cartes)

    def __repr__(self):
        return f"<Paquet {len(self._cartes)} cartes>"

    def melanger(self):
        random.shuffle(self._cartes)

    def couper(self):
        n = random.randint(1, len(self._cartes) - 1)
        self._cartes = self._cartes[n:] + self._cartes[:n]

    def piocher(self):
        if not self._cartes:
            raise IndexError("Le paquet est vide.")
        return self._cartes.pop(0)

    def distribuer(self, joueurs, cartes):
        if joueurs * cartes > len(self._cartes):
            raise ValueError(
                f"Pas assez de cartes : {len(self._cartes)} disponibles, "
                f"{joueurs * cartes} demandées."
            )
        mains = [[] for _ in range(joueurs)]
        for _ in range(cartes):
            for main in mains:
                main.append(self.piocher())
        return mains
