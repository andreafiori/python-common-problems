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
    def doublefactorial(n):
        """
        Calculate double factorial
        :param n:
        :return:
        """
        return 1 if n <= 0 else n * self.doublefactorial(n - 2)

    # Without using recursion
    # def calculate(self, n):
    #     fact = 1
    #     for i in range(1, n + 1):
    #         fact = fact * i
    #     return fact

    # Using math
    # def calculate(self, n):
    #     math.factorial(5.6)