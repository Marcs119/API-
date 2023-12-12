import unittest
from iva import calculariva

class TestsCalcularIva(unittest.TestCase):
    def test_calcular_iva_100(self):
        result = calculariva(100)
        self.assertEqual(result, 21)
        
if __name__ == '__main__':
    unittest.main()
