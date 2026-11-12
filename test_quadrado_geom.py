import unittest

from quadrado_geom import quadrado_geom


class TestQuadradoGeom(unittest.TestCase):
    def test_medidas_para_lados_positivos(self):
        for lado, area, perimetro, diagonal in (
            (5.0, 25.0, 20.0, 7.0710678118654755),
            (2.0, 4.0, 8.0, 2.8284271247461903),
        ):
            with self.subTest(lado=lado):
                resultado = quadrado_geom(lado)
                self.assertIsInstance(resultado, dict)
                self.assertEqual(resultado["area"], area)
                self.assertEqual(resultado["perimetro"], perimetro)
                self.assertAlmostEqual(resultado["diagonal"], diagonal, delta=1e-9)

    def test_rejeita_lado_zero(self):
        with self.assertRaises(ValueError):
            quadrado_geom(0.0)

    def test_rejeita_lados_negativos(self):
        for lado in (-1.0, -5.0):
            with self.subTest(lado=lado):
                with self.assertRaises(ValueError):
                    quadrado_geom(lado)
