class StringUtil:
	@staticmethod
	def isPalindrome(n):
		return str(n) == str(n)[::-1]