import unittest
from carte import Carte


class TestCarteCreation(unittest.TestCase):
    def test_creation_valeur_int(self):
        c = Carte(3, 'COEUR')
        self.assertEqual(c.valeur, 3)
        self.assertEqual(c.couleur, 'COEUR')

    def test_creation_valeur_figuree(self):
        c = Carte('ROI', 'PIQUE')
        self.assertEqual(c.valeur, 'ROI')
        self.assertEqual(c.couleur, 'PIQUE')

    def test_creation_toutes_couleurs(self):
        for couleur in ['COEUR', 'PIQUE', 'CARREAU', 'TREFLE']:
            c = Carte(1, couleur)
            self.assertEqual(c.couleur, couleur)

    def test_creation_toutes_valeurs(self):
        for valeur in list(range(1, 11)) + ['VALET', 'DAME', 'ROI']:
            c = Carte(valeur, 'COEUR')
            self.assertEqual(c.valeur, valeur)


class TestCarteValeurInvalide(unittest.TestCase):
    def test_valeur_zero(self):
        with self.assertRaises(ValueError):
            Carte(0, 'COEUR')

    def test_valeur_onze_int(self):
        with self.assertRaises(ValueError):
            Carte(11, 'COEUR')

    def test_valeur_string_inconnue(self):
        with self.assertRaises(ValueError):
            Carte('AS', 'COEUR')

    def test_couleur_invalide(self):
        with self.assertRaises(ValueError):
            Carte(5, 'JOKER')

    def test_couleur_minuscule(self):
        with self.assertRaises(ValueError):
            Carte(5, 'coeur')


class TestCarteMutateurs(unittest.TestCase):
    def test_mutateur_valeur_valide(self):
        c = Carte(1, 'COEUR')
        c.valeur = 'DAME'
        self.assertEqual(c.valeur, 'DAME')

    def test_mutateur_valeur_invalide(self):
        c = Carte(1, 'COEUR')
        with self.assertRaises(ValueError):
            c.valeur = 99

    def test_mutateur_couleur_valide(self):
        c = Carte(1, 'COEUR')
        c.couleur = 'TREFLE'
        self.assertEqual(c.couleur, 'TREFLE')

    def test_mutateur_couleur_invalide(self):
        c = Carte(1, 'COEUR')
        with self.assertRaises(ValueError):
            c.couleur = 'ROUGE'


class TestCartePoints(unittest.TestCase):
    def test_points_valeurs_numeriques(self):
        for i in range(1, 11):
            self.assertEqual(Carte(i, 'COEUR').points(), i)

    def test_points_valet(self):
        self.assertEqual(Carte('VALET', 'COEUR').points(), 11)

    def test_points_dame(self):
        self.assertEqual(Carte('DAME', 'COEUR').points(), 12)

    def test_points_roi(self):
        self.assertEqual(Carte('ROI', 'COEUR').points(), 13)


class TestCarteRepr(unittest.TestCase):
    def test_repr_int(self):
        self.assertEqual(repr(Carte(3, 'COEUR')), '<Carte 3 de COEUR>')

    def test_repr_figuree(self):
        self.assertEqual(repr(Carte('ROI', 'PIQUE')), '<Carte ROI de PIQUE>')

    def test_print_utilise_repr(self):
        import io, sys
        out = io.StringIO()
        sys.stdout = out
        print(Carte(3, 'COEUR'))
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue().strip(), '<Carte 3 de COEUR>')


if __name__ == '__main__':
    unittest.main()
