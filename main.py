import string
import sys
from JConstants import *
from JStack import JStack
from JOperations import JOperations
from JUtils import JUtils


class JSONParser:

    def __init__(self,app_mode=None):
        self.__stack = JStack()
        self.__oper = JOperations()
        self.__utils = JUtils()


    def json_to_tokens(self, json_str=None):
        parse_str = []
        words = ''
        if json_str:
            for i in range(len(json_str)):
                if json_str[i] in JSON_SYM:
                    if words:
                        parse_str.append(words)
                    if json_str[i] == '{' or json_str[i] == '}':
                        parse_str.append(json_str[i])
                    elif json_str[i] == ':' or json_str[i] == ',':
                        parse_str.append(json_str[i])
                    elif json_str[i] == '[' or json_str[i] == ']':
                        parse_str.append(json_str[i])
                    words = ''
                elif json_str[i] in CHAR_ALPH_LOW or json_str[i] in CHAR_ALPH_HIG  or json_str[i] in NUM or json_str[i] in SPl_SYM:
                    words += json_str[i]
        return parse_str


    def operOnTokens(self, tokens):
        # tokens = [ "{", "sunil", ":", "{", "dob", ":", "23-09-2001", "addr", ":", "bhopal", "}", ",", "vivek", ":", "[", "kallu", "]", "}" ]
        for i in range(0, len(tokens)):
            self.__stack.push(tokens[i])
            if self.__utils.isCloseing(tokens[i]):
                self.__stack.show('showing stack push')
                result = self.convertBrackToObject()
        print("\nfinal result:", result)



    # converts '{' to '}' to object
    def convertBrackToObject(self):
        tmpArr = []
        while not self.__stack.isEmpty():
            item = self.__stack.pop()
            tmpArr.append(item)
            if self.__utils.isOpening(item):
                obj = self.__oper.toObject(tmpArr)
                if self.__stack.isEmpty():
                    return obj
                self.__stack.push(obj)
                self.__stack.show("showing stack..")
                tmpArr = []
                break

if __name__ == '__main__':
    jsonFile = sys.argv[1]
    with open(jsonFile, 'r') as file:
        data = file.read().replace('\n', '')
        jsonParser = JSONParser()
        tokens = jsonParser.json_to_tokens(data)
        jsonParser.operOnTokens(tokens)
