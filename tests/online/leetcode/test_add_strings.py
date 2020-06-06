import unittest

from src.online.leetcode.add_strings import AddStrings


class AddStringsTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(AddStrings.solution("12", "13"), "2.55")
