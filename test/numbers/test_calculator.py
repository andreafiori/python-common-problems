import unittest
from src.numbers.calculator import Calculator

class CalculatorTest(unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()

	def test_sum(self):
		sum = self.calc.add(1, 3)
		self.assertEqual(sum, 4)
	
	def test_subtract(self):
		subtract = self.calc.subtract(4, 3)
		self.assertEqual(subtract, 1)

	def test_divide(self):
		divided = self.calc.divide(12, 3)
		self.assertEqual(divided, 4)

	def test_divide_by_zero_exception(self):
		with self.assertRaises(Exception) as context:
			self.calc.divide(4, 0)