import unittest
from src.algorithms.strings.string_util import StringUtil

class StringUtilTest(unittest.TestCase):
    def test_is_palindrom_is_true(self):
        self.assertTrue(StringUtil.is_palindrome('deified'))

    def test_is_palindrom_is_false(self):
        self.assertFalse(StringUtil.is_palindrome('asso'))

    def test_reverse(self):
        self.assertEqual(StringUtil.reverse('hello world'), 'dlrow olleh')
