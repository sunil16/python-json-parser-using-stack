import string

CONT_VAl = {'null':None, 'true':True, 'false':False}
SPl_SYM = {'#':True}
NUM = {'0':True, '1':True, '2':True, '3':True , '4':True, '5':True, '6':True, '7':True, '8':True,'9':True}
CHAR_ALPH_LOW = dict(zip(string.ascii_lowercase, range(1,27)))
CHAR_ALPH_HIG = dict(zip(string.ascii_uppercase, range(1,27)))
JSON_SYM = { ',':True , ':':True , '[':True, ']': True, '{':True ,'}':True, '"':True, "'":True }
JSON_WHITESPACE = { ' ':True, '\t':True, '\b':True, '\n':True, '\r':True }

JSON_OPEN_BRACE = '{'
JSON_CLOSE_BRACE = '}'

JSON_OPEN_BRACKET = '['
JSON_CLOSE_BRACKET = ']'

JSON_SEPERATORS = {
	":": True,
	",": True
}

JSON_OPENING = {
	"{": True,
	"[": True
}

JSON_CLOSEING = { 
	"}": True, 
	"]": True 
}