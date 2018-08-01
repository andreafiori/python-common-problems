import unittest
from src.strings.balancedparentheses import BalancedParentheses

class BalancedParenthesisTest(unittest.TestCase):
    def setUp(self):
        self.bal = BalancedParentheses()

    def test_check(self):
        self.assertTrue(self.bal.check('((()))'))

    def test_check_fails(self):
        self.assertFalse(self.bal.check('(()'))
