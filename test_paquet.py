import unittest
from paquet import Paquet
from carte import Carte


class TestPaquetCreation(unittest.TestCase):
    def test_taille_initiale(self):
        p = Paquet()
        self.assertEqual(len(p), 52)

    def test_toutes_cartes_sont_des_cartes(self):
        p = Paquet()
        for carte in p._cartes:
            self.assertIsInstance(carte, Carte)

    def test_pas_de_doublons(self):
        p = Paquet()
        cles = [(c.valeur, c.couleur) for c in p._cartes]
        self.assertEqual(len(cles), len(set(cles)))

    def test_repr(self):
        p = Paquet()
        self.assertEqual(repr(p), '<Paquet 52 cartes>')


class TestPaquetMelanger(unittest.TestCase):
    def test_taille_inchangee_apres_melange(self):
        p = Paquet()
        p.melanger()
        self.assertEqual(len(p), 52)

    def test_memes_cartes_apres_melange(self):
        p = Paquet()
        avant = {(c.valeur, c.couleur) for c in p._cartes}
        p.melanger()
        apres = {(c.valeur, c.couleur) for c in p._cartes}
        self.assertEqual(avant, apres)


class TestPaquetCouper(unittest.TestCase):
    def test_taille_inchangee_apres_coupe(self):
        p = Paquet()
        p.couper()
        self.assertEqual(len(p), 52)

    def test_memes_cartes_apres_coupe(self):
        p = Paquet()
        avant = {(c.valeur, c.couleur) for c in p._cartes}
        p.couper()
        apres = {(c.valeur, c.couleur) for c in p._cartes}
        self.assertEqual(avant, apres)


class TestPaquetPiocher(unittest.TestCase):
    def test_piocher_retourne_une_carte(self):
        p = Paquet()
        c = p.piocher()
        self.assertIsInstance(c, Carte)

    def test_piocher_reduit_taille(self):
        p = Paquet()
        p.piocher()
        self.assertEqual(len(p), 51)

    def test_piocher_paquet_vide(self):
        p = Paquet()
        for _ in range(52):
            p.piocher()
        with self.assertRaises(IndexError):
            p.piocher()


class TestPaquetDistribuer(unittest.TestCase):
    def test_nombre_joueurs_et_cartes(self):
        p = Paquet()
        mains = p.distribuer(joueurs=4, cartes=5)
        self.assertEqual(len(mains), 4)
        for main in mains:
            self.assertEqual(len(main), 5)

    def test_cartes_retirees_du_paquet(self):
        p = Paquet()
        p.distribuer(joueurs=4, cartes=5)
        self.assertEqual(len(p), 52 - 4 * 5)

    def test_distribution_tour_a_tour(self):
        p = Paquet()
        # On fixe l'ordre pour vérifier la distribution à tour de rôle
        premiere = p._cartes[0]
        deuxieme = p._cartes[1]
        mains = p.distribuer(joueurs=2, cartes=1)
        self.assertEqual(mains[0][0], premiere)
        self.assertEqual(mains[1][0], deuxieme)

    def test_distribuer_pas_assez_de_cartes(self):
        p = Paquet()
        with self.assertRaises(ValueError):
            p.distribuer(joueurs=10, cartes=6)


if __name__ == '__main__':
    unittest.main()
