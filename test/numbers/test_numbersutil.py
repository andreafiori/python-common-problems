import unittest
from src.numbersutil import NumbersUtil

class NumbersUtilTest(unittest.TestCase):
	def test_isPalindrome_as_true(self):
		self.assertTrue(NumbersUtil.isPalindrome(121))

	def test_isPalindrome_as_false(self):
		self.assertFalse(NumbersUtil.isPalindrome(567))

	def test_factorial(self):
		self.assertEqual(NumbersUtil.factorial(4), 24)

	def test_check_convert_base_two(self):
		self.assertEqual(NumbersUtil.convert(25, 2), '11001')

	def test_check_convert_base_twob(self):
		self.assertEqual(NumbersUtil.convert(25, 16), '19')

	def test_find_smallest_divisor(self):
		self.assertEqual(NumbersUtil.smallestDivisor(75), 3)