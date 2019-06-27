from JConstants import *

## json utilities
class JUtils:

	def reverseArray(self, arr):
		return arr[::-1]


	def isCloseing(self, char):
		if char in JSON_CLOSEING:
			return JSON_CLOSEING[char]
		else:
			return False


	def isOpening(self, char_obj):
		if type(char_obj) is str:
			if char_obj in JSON_OPENING:
				return JSON_OPENING[char_obj]
		return False



	






