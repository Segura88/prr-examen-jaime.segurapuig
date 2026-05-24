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

    def test_cadena_vacia(self):
        self.assertEqual(procesar_mensaje(""), "ERROR")

    def test_cadena_sin_comando(self):
        self.assertEqual(procesar_mensaje(": Hola Mundo"), "ERROR")

    def test_numero_en_vez_de_cadena(self):
        self.assertEqual(procesar_mensaje(12345), "ERROR")

    def test_none(self):
        self.assertEqual(procesar_mensaje(None), "ERROR")

    def test_vocales(self):
        self.assertEqual(procesar_mensaje("VOCALES: Hola Mundo"), "VOCALES:4")

    def test_vocales_sin_vocales(self):
        self.assertEqual(procesar_mensaje("VOCALES: Hll Mnd"), "VOCALES:0")

    def test_vocales_con_mayusculas(self):
        self.assertEqual(procesar_mensaje("VOCALES: HOLA MUNDO"), "VOCALES:4")

    def test_vocales_con_espacios(self):
        self.assertEqual(procesar_mensaje("VOCALES:   HOLA MUNDO   "), "VOCALES:4")

    def test_vocales_vacio(self):
        self.assertEqual(procesar_mensaje("VOCALES: "), "VOCALES:0")
