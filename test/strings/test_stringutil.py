import unittest
from src.strings.stringutil import StringUtil

class StringUtilTest(unittest.TestCase):
	def test_is_palindrom_is_true(self):
		self.assertTrue( StringUtil.isPalindrome('deified') )

	def test_is_palindrom_is_false(self):
		self.assertFalse( StringUtil.isPalindrome('asso') )
