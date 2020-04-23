import math

"""
Factorial https://en.wikipedia.org/wiki/Factorial
Double Factorial https://en.wikipedia.org/wiki/Double_factorial
"""


class Factorial(object):
    @staticmethod
    def calculate(n):
        """
        Calculate factorial of a number
        :param n:
        :return:
        """
        return 1 if (n == 1 or n == 0) else n * Factorial.calculate(n - 1)

    @staticmethod
    def double_factorial(n):
        """
        Calculate double factorial
        :param n:
        :return:
        """
        return 1 if n <= 0 else n * Factorial.double_factorial(n - 2)

    # Without using recursion
    # def calculate(self, n):
    #     fact = 1
    #     for i in range(1, n + 1):
    #         fact = fact * i
    #     return fact

    @staticmethod
    def calculate_using_math(num):
        """
        Calculate Factorial
        :param num: int
        :return: int
        """
        math.factorial(num)

    @staticmethod
    def factorial_not_recursive(number):
        """
        Calculate factorial of a number with no recursion
        :param number: int
        :return: int
        """
        result = 1
        while number >= 1:
            result = result * number
            number = number - 1
        return result
