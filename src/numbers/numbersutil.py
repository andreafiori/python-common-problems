from src.datastructures.stack import Stack

"""
Common function for working with numbers
"""
class NumbersUtil:
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(n):
        temp = n
        rev = 0
        while(n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n = n//10
        if (temp==rev):
            return True
        else:
            return False

    @staticmethod
    def factorial(n):
        result = 1
        i = n * (n -1)
        while n >= 1:
            result = result * n
            n = n - 1
        return result

    def factorial_recursive(self, n):
        if n < 1: # base case
            return 1
        else:
            returnNumber = n * self.factorial_recursive( n - 1 )  # recursive call
            # print(str(n) + '! = ' + str(returnNumber))
            return returnNumber

    @staticmethod
    def convert(decNumber,base):
        digits = "0123456789ABCDEF"

        remstack = Stack()

        while decNumber > 0:
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base

        newString = ""
        while not remstack.is_empty():
            newString = newString + digits[remstack.pop()]

        return newString

    @staticmethod
    def smallest_divisor(n):
        a=[]
        for i in range(2,n+1):
            if(n%i==0):
                a.append(i)
        a.sort()
        return a[0]

    @staticmethod
    def calculate_divisors(n):
        a = []
        for i in range(1, n+1):
            if (n % i == 0):
                a.append(i)
        return a

    @staticmethod
    def is_prime(num):
        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2,num):
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
