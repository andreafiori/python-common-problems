from src.datastructures.stack import Stack

class NumbersUtil:
	@staticmethod
	def isPalindrome(n):
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

	@staticmethod
	def convert(decNumber,base):
		digits = "0123456789ABCDEF"

		remstack = Stack()

		while decNumber > 0:
			rem = decNumber % base
			remstack.push(rem)
			decNumber = decNumber // base

		newString = ""
		while not remstack.isEmpty():
			newString = newString + digits[remstack.pop()]

		return newString

	@staticmethod
	def smallestDivisor(n):
		a=[]
		for i in range(2,n+1):
			if(n%i==0):
				a.append(i)
		a.sort()
		return a[0]