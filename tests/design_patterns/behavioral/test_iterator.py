import unittest

from src.design_patterns.behavioral.iterator import count_to


class IteratorTest(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(_build_dict_count_to_two(), ['one', 'two'])


def _build_dict_count_to_two():
    # Build a dictionary with the generator values
    generator_list = []
    for number in count_to(2):
        generator_list.append(number)
    return generator_list