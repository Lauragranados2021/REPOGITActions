import unittest
from Numero import ingresar_numero

class TestIngresarNumero(unittest.TestCase):
    #when
    def test_ingresar_numero_5(self):
        resultado = ingresar_numero()
        #that
        self.assertEqual(resultado, 5)
