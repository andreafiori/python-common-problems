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
        return True if temp == rev else False

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
    def smallest_divisor(num):
        a = []
        for i in range(2, num + 1):
            if (num % i) == 0:
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
        '''check if integer number is a prime'''

        # make sure n is a positive integer
        num = abs(int(num))

        # 0 and 1 are not primes
        if num < 2:
            return False

        # 2 is the only even prime number
        if num == 2: 
            return True    

        # all other even numbers are not primes
        if not num & 1: 
            return False

        # range starts with 3 and only needs to go up 
        # the square root of nnumor all odd numbers
        for x in range(3, int(num ** 0.5) + 1, 2):
            if num % x == 0:
                return False

        return True