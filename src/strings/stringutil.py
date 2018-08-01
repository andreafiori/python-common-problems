"""
String Utils
"""
class StringUtil:
    def __init__(self):
        pass

    @staticmethod
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
