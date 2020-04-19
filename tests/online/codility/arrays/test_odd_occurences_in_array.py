import unittest
from src.online.codility.arrays.odd_occurences_in_array import OddOccurrencesInArray

class TestOddOccurencesInArray(unittest.TestCase):

    def setup_class(self):
        self.oddOccurrencesInArray = OddOccurrencesInArray()

    """
    TODO: test print value
    def test_sample_generation(self):
        print self.oddOccurrencesInArray.gen_array(5, 1)
    """

    def test_example1(self):
        arr = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, self.oddOccurrencesInArray.solution(arr))

    def test_simple1(self):
        """simple test n=5"""
        arr = self.oddOccurrencesInArray.gen_array(5, 4)
        self.assertEqual(4, self.oddOccurrencesInArray.solution(arr))

    def test_simple2(self):
        """simple test n=11"""
        arr = self.oddOccurrencesInArray.gen_array(11, 4)
        self.assertEqual(4, self.oddOccurrencesInArray.solution(arr))

    def test_extreme_single_item(self):
        """list containing one item"""
        self.assertEqual(42, self.oddOccurrencesInArray.solution([42]))

    def test_small1(self):
        """small random test n=201"""
        arr = self.oddOccurrencesInArray.gen_array(201, 42)
        self.assertEqual(42, self.oddOccurrencesInArray.solution(arr))

    def test_small2(self):
        """small random test n=601"""
        arr = self.oddOccurrencesInArray.gen_array(601, 4242)
        self.assertEqual(4242, self.oddOccurrencesInArray.solution(arr))

    def test_medium1(self):
        """medium random test n=2001"""
        arr = self.oddOccurrencesInArray.gen_array(2001, 100)
        self.assertEqual(100, self.oddOccurrencesInArray.solution(arr))

    def test_medium2(self):
        """medium random test n=100,003"""
        arr = self.oddOccurrencesInArray.gen_array(100003, 500000)
        self.assertEqual(500000, self.oddOccurrencesInArray.solution(arr))

    def test_big1(self):
        """big random test n=999,999, multiple repetitions"""
        arr = self.oddOccurrencesInArray.gen_array(100003, 700)
        self.assertEqual(700, self.oddOccurrencesInArray.solution(arr))

    def test_big2(self):
        """big random test n=999,999"""
        arr = self.oddOccurrencesInArray.gen_array(999999, 5000111222)
        self.assertEqual(5000111222, self.oddOccurrencesInArray.solution(arr))