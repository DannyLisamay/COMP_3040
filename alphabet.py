#Danny Lisamay
#
#alphabet class
#alphabet is a list of characters
import character
class alphabet:
    def __init__(self, a = []):
        self.a = a
    #toString
    def __str__(self):
        #getCharater and format into a string
        #binary ex. [(0),(1)]
        strAlphabet = "["
        if len(self.a) != 0:
            for x in range(len(self.a)):
                strAlphabet += "(" + self.a[x].getCharater() + ")"
                if x != len(self.a) - 1:
                    strAlphabet += ","
        else:
            strAlphabet += '\u00D8'
        strAlphabet += "]"
        return strAlphabet

        #generate Nth string
