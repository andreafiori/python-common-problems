import unittest
import random
from src.online.codility.tape_equilibrium import TapeEquilibrium

class TestTapeEquilibrium(unittest.TestCase):

    def setup_class(self):
        self.tapeEquilibrium = TapeEquilibrium()

    def test_example1(self):
        self.assertEqual(self.tapeEquilibrium.solution([3, 1, 2, 4, 3]), 1)

    def test_simple(self):
        self.assertEqual(self.tapeEquilibrium.solution([1,2]), 1)

    def test_double(self):
        self.assertEqual(self.tapeEquilibrium.solution([-1000, 1000]), 2000)

    def test_random(self):
        N = random.randint(*TapeEquilibrium.N_RANGE)
        arr = [random.randint(*TapeEquilibrium.ELEMENT_RANGE) for _ in range(N)]
        """ TODO: test followin instruction """
        """ print N, self.tapeEquilibrium(arr), arr """

    def test_maximum(self):
        arr = [random.randint(*TapeEquilibrium.ELEMENT_RANGE) for _ in range(100000)]
        """ TODO: test followin instruction """
        """ print 100000, self.tapeEquilibrium(arr), arr """
