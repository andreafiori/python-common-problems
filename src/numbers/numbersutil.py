from src.datastructures.stack import Stack

"""
Numbers Utils
"""
class NumbersUtil:
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(number):
        temp = number
        rev = 0
        while number > 0:
            dig = number % 10
            rev = rev * 10 + dig
            number = number//10
        if temp == rev:
            return True
        else:
            return False

    @staticmethod
    def factorial(number):
        result = 1
        while number >= 1:
            result = result * number
            number = number - 1
        return result

    def factorial_recursive(self, number):
        if number < 1: # base case
            return 1
        else:
            return_number = number * self.factorial_recursive(number - 1)  # recursive call
            # print(str(n) + '! = ' + stragr(returnNumber))
            return return_number

    @staticmethod
    def convert(dec_number, base):
        digits = "0123456789ABCDEF"

        remstack = Stack()

        while dec_number > 0:
            rem = dec_number % base
            remstack.push(rem)
            dec_number = dec_number // base

        new_string = ""
        while not remstack.is_empty():
            new_string = new_string + digits[remstack.pop()]

        return new_string

    @staticmethod
    def smallest_divisor(n):
        a = []
        for i in range(2, n + 1):
            if (n % i) == 0:
                a.append(i)
        a.sort()
        return a[0]

    @staticmethod
    def calculate_divisors(number):
        a = []
        for i in range(1, number + 1):
            if (number % i) == 0:
                a.append(i)
        return a

    @staticmethod
    def is_prime(num):
        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # print(num,"is not a prime number")
                    # print(i,"times",num//i,"is",num)
                    return True
                else:
                    return True
        # if input number is less than
        # or equal to 1, it is not prime
        else:
            return False
