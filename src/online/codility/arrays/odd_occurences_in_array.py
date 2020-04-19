import random


class OddOccurrencesInArray(object):
    # the largest length array we have to handle
    MAX_LENGTH = 1000000

    def solution(self, arr):
        """
        Find the value that does not have a match in an odd sized array
        :param arr: an array of integers with an odd number of elements
        :param N: length of the array
        :return: the one element which does not have a complementary element
        """
        # protect against crazy inputs
        if not isinstance(arr, list):
            raise TypeError("Input must be a list of integers")
        if len(arr) < 1:
            raise ValueError("Input list must not be empty")
        if len(arr) > self.MAX_LENGTH:
            raise ValueError("Input list must not be longer than %s" % self.MAX_LENGTH)

        # dictionary of keys in need of a match
        unmatched = dict()

        # for every element
        for element in arr:
            # try removing it's match
            try:
                del unmatched[element]
            except KeyError:
                # else add it
                unmatched[element] = True

        # if one unmatched item
        if len(unmatched) == 1:
            return unmatched.keys()[0]
        else:
            raise Exception("Expected one unmatched item, but have this: %s" % unmatched)

    def gen_array(self, L, odd):
        """generate a list of sample data: random integers in pairs
        :param L: the length of the list is double this int
        :param odd: the odd integer out
        """
        arr = []
        for _ in range((L - 1) / 2):
            val = random.randint(1, self.MAX_LENGTH)
            arr.extend((val, val))
        arr.append(odd)
        random.shuffle(arr)
        return arr
