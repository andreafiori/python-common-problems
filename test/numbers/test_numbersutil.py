import unittest
from src.numbers.numbersutil import NumbersUtil

class NumbersUtilTest(unittest.TestCase):
    def test_is_palindrome_as_true(self):
        self.assertTrue(NumbersUtil.is_palindrome(121))

    def test_is_palindrome_as_false(self):
        self.assertFalse(NumbersUtil.is_palindrome(567))

    def test_factorial(self):
        self.assertEqual(NumbersUtil.factorial(4), 24)

    def test_factorial_recursive(self):
        util = NumbersUtil()
        self.assertEqual(util.factorial_recursive(4), 24)

    def test_check_convert_base_two(self):
        self.assertEqual(NumbersUtil.convert(25, 2), '11001')

    def test_check_convert_base_hex(self):
        self.assertEqual(NumbersUtil.convert(25, 16), '19')

    def test_find_smallest_divisor(self):
        self.assertEqual(NumbersUtil.smallestDivisor(75), 3)
