class Factorial:
	@staticmethod
	def calculate(n):
		result = 1
		i = n * (n -1)
		while n >= 1:
			result = result * n
			n = n - 1
		return result
