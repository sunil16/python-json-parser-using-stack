

class JStack:

	def __init__(self):
		self.__array = []


	def push(self, value):
		self.__array.append(value)


	def pop(self):
	    if self.isEmpty():
	    	return NULL
	    else:
	    	return self.__array.pop()


	def isEmpty(self):
	 	return len(self.__array) == 0


	def show(self, msg=''):
		# print(msg, self.__array)
		pass
