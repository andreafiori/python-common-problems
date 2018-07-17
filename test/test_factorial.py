import unittest
from src.factorial import Factorial

class FactorialTest(unittest.TestCase):
	def test_calculate(self):
		fact = Factorial.calculate(4)
		self.assertEqual(fact, 24)