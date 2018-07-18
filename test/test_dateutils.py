import unittest
from src.dateutils import DateUtils

class DateUtilsTest(unittest.TestCase):
	def test_isLeapYear(self):
		self.assertTrue(DateUtils.isLeapYear(2004))