"""
Fibonacci math
"""
class Fibonacci(object):
    def calculate(self, n):
        """
        Function for nth Fibonacci number
        :param n: int
        :return:
        """
        if n < 0:
            raise Exception("Invalid input")
            # First Fibonacci number is 0
        elif n == 1:
            return 0
            # Second Fibonacci number is 1
        elif n == 2:
            return 1
        else:
            return self.calculate(n - 1) + self.calculate(n - 2)
