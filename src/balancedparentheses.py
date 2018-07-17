from src.stack import Stack

class BalancedParentheses:
	@staticmethod
	def check(symbolString):
		s = Stack()
		balanced = True
		index = 0
		strLen = len(symbolString)

		if (strLen % 2) != 0:
			return False

		while index < strLen and balanced:
			symbol = symbolString[index]
			if symbol == "(":
				s.push(symbol)
			else:
				if s.isEmpty():
					balanced = False
				else:
					s.pop()

			index = index + 1

		if balanced and s.isEmpty():
			return True
		else:
			return False