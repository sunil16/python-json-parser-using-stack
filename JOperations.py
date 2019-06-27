from JUtils import JUtils
from JConstants import *
from JLogs import log

## perform basic operations
class JOperations:

	def __init__(self):
		self.__utils = JUtils()


	def isString(self, obj):
		return type(obj) is str


	def removeSymbols(self, tokens):
		splitSymbols =  {**JSON_SEPERATORS, **JSON_OPENING, **JSON_CLOSEING} 
		result = []
		for token in tokens:
			if self.isString(token):
				if token not in splitSymbols:
					result.append(token)
			else:
				result.append(token)
		return result



	def getTypeOfList(self, arr): # { 0: array, 1: dict, 2: None, 3: error }
		if len(arr) == 0:
			return 2
		if len(arr) > 0:
			firstEle = arr[0]
			lastEle = arr[len(arr)-1]
			if firstEle is JSON_OPEN_BRACE and lastEle is JSON_CLOSE_BRACE:
				return 1
			if firstEle is JSON_OPEN_BRACKET and lastEle is JSON_CLOSE_BRACKET:
				return  0
		return 3


	def toObject(self, arr):
		arr = self.__utils.reverseArray(arr)
		log('need to convert this object', arr)
		objType = self.getTypeOfList(arr)
		if objType == 0:
			return self.toArray(arr)
		if objType == 1:
			return self.toDict(arr)
		if objType == 2:
			log('no data fount to convert into object')
		if objType == 3:
			log('some error fount while checking braket pairs here:', arr)
		return []


	def toArray(self, arr):
		log('It is array', arr)
		arr = self.removeSymbols(arr)
		log("arr is:", arr)
		return arr


	def toDict(self, arr):
		log('It is dictinoary', arr)
		arr = self.removeSymbols(arr)
		log('after removing symbols', arr)
		arr = dict(zip(arr[::2], arr[1::2]))
		log(obj=arr)
		return arr


	# need to add
	def toInt(self, str):
		return 0

	# need to add
	def toDouble(self, str):
		return 0.0

	# need to add
	def toString(self, str):
		return ""







