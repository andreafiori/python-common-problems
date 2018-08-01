from src.datastructures.stack import Stack

"""
Check if parenthesis are balanced
"""
class BalancedParentheses:
    def __init__(self):
        pass

    @staticmethod
    def check(symbol_string):
        s = Stack()
        balanced = True
        index = 0
        strLen = len(symbol_string)

        if (strLen % 2) != 0:
            return False

        while index < strLen and balanced:
            symbol = symbol_string[index]
            if symbol == "(":
                s.push(symbol)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    s.pop()

            index = index + 1

        return True if (balanced and s.is_empty()) else False
