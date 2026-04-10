VALEURS_VALIDES = list(range(1, 11)) + ['VALET', 'DAME', 'ROI']
COULEURS_VALIDES = ['COEUR', 'PIQUE', 'CARREAU', 'TREFLE']


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"<Carte {self._valeur} de {self._couleur}>"

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, valeur):
        if valeur not in VALEURS_VALIDES:
            raise ValueError(
                f"Valeur invalide : {valeur!r}. "
                f"Valeurs acceptées : {VALEURS_VALIDES}"
            )
        self._valeur = valeur

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, couleur):
        if couleur not in COULEURS_VALIDES:
            raise ValueError(
                f"Couleur invalide : {couleur!r}. "
                f"Couleurs acceptées : {COULEURS_VALIDES}"
            )
        self._couleur = couleur

    def points(self):
        if isinstance(self._valeur, int):
            return self._valeur
        return {'VALET': 11, 'DAME': 12, 'ROI': 13}[self._valeur]
