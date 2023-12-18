# Testes unitários para a calculadora no arquivo main.py

import unittest
from main import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
  def test_soma(self):
    self.assertEqual(soma(2, 2), 4)

  def test_subtracao(self):
    self.assertEqual(subtracao(2, 2), 0)

  def test_multiplicacao(self):
    self.assertEqual(multiplicacao(2, 2), 4)

  def test_divisao(self):
    self.assertEqual(divisao(2, 2), 1)

  # def test_divisao_por_zero(self):
    # self.assertEqual(divisao(2, 2), "Não é possível dividir por zero")

if __name__ == '__main__':
  unittest.main()