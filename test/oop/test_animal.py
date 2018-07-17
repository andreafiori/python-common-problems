import unittest
from src.oop.cat import Cat

class CatTest(unittest.TestCase):
	def test_say_something(self):
		cat = Cat()
		self.assertEqual(cat.say_something(), "I'm an animal! Miauuu")
