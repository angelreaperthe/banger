# teste-calculadora.py
import unittest
from calculadora import soma, subtrai, multiplica, divide

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3, "Erro: 1 + 2 deveria ser 3")
        print("Teste soma(1, 2) == 3: PASSOU")

        self.assertEqual(soma(-1, 1), 0, "Erro: -1 + 1 deveria ser 0")
        print("Teste soma(-1, 1) == 0: PASSOU")

        self.assertEqual(soma(-1, -1), -2, "Erro: -1 + (-1) deveria ser -2")
        print("Teste soma(-1, -1) == -2: PASSOU")

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 5), 5, "Erro: 10 - 5 deveria ser 5")
        print("Teste subtrai(10, 5) == 5: PASSOU")

        self.assertEqual(subtrai(-1, -1), 0, "Erro: -1 - (-1) deveria ser 0")
        print("Teste subtrai(-1, -1) == 0: PASSOU")

        self.assertEqual(subtrai(0, 1), -1, "Erro: 0 - 1 deveria ser -1")
        print("Teste subtrai(0, 1) == -1: PASSOU")

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 7), 21, "Erro: 3 * 7 deveria ser 21")
        print("Teste multiplica(3, 7) == 21: PASSOU")

        self.assertEqual(multiplica(-1, 1), -1, "Erro: -1 * 1 deveria ser -1")
        print("Teste multiplica(-1, 1) == -1: PASSOU")

        self.assertEqual(multiplica(0, 10), 0, "Erro: 0 * 10 deveria ser 0")
        print("Teste multiplica(0, 10) == 0: PASSOU")

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5, "Erro: 10 / 2 deveria ser 5")
        print("Teste divide(10, 2) == 5: PASSOU")

        self.assertEqual(divide(-10, 2), -5, "Erro: -10 / 2 deveria ser -5")
        print("Teste divide(-10, 2) == -5: PASSOU")

        with self.assertRaises(ValueError, msg="Erro: divisão por zero deveria gerar ValueError"):
            divide(10, 0)
        print("Teste divide(10, 0) levantou ValueError: PASSOU")

if __name__ == '__main__':
    print("Iniciando execução dos testes da calculadora...\n")
    unittest.main(verbosity=2)

