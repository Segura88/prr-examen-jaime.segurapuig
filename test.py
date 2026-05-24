import unittest
from logica import procesar_mensaje

class Test(unittest.TestCase):
    def test_invertir(self):
        self.assertEqual(procesar_mensaje("INVERTIR: Hola Mundo"), "odnuM aloH")

    def test_invertir_con_espacios(self):
        self.assertEqual(procesar_mensaje("INVERTIR:   Hola Mundo   "), "odnuM aloH")

    def test_invertir_vacio(self):
        self.assertEqual(procesar_mensaje("INVERTIR: "), "")

    def test_comando_desconocido(self):
        self.assertEqual(procesar_mensaje("DESCONOCIDO: Hola Mundo"), "ERROR")

    def test_comando_sin_parametros(self):
        self.assertEqual(procesar_mensaje("INVERTIR"), "ERROR")