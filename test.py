import unittest
from logica import procesar_mensaje

class Test(unittest.TestCase):
    def test_invertir(self):
        self.assertEqual(procesar_mensaje("INVERTIR Hola Mundo"), "odnuM aloH")
        