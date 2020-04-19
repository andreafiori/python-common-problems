import unittest

class TestStack(unittest.TestCase):
    def testCompareTwoLists(self):
        actual = ['bl', 'direction', 'day']
        assert all([a == b for a, b in zip(actual, ['bl', 'direction', 'day'])])