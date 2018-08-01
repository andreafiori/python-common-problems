import unittest
from src.dateutils import DateUtils

class DateUtilsTest(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(DateUtils.is_leap_year(2004))
