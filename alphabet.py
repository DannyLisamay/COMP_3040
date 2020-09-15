#Danny Lisamay
#9/11
#alphabet class
#alphabet is a list of characters
#9/13
#created lexicographic function
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

    #strings class
    class strings:
        def __init__(self, s: list):
            self.s = s
        def addChar(self, c):
            self.s.append(c)
        def __str__(self):
            #getCharater and format into a string
            #binary ex. [(0),(1)]
            str = "String = ["
            if len(self.s) != 0:
                for x in range(len(self.s)):
                    str += "(" + self.s[x].getCharater() + ")"
                    if x != len(self.s) - 1:
                        str += ","
            else:
                str += '\u00D8'
            str += "]"
            return str

    #generate Nth string lexicographic order
    def lexicographic(self, n):
        n0 = n
        s = self.strings(s = [])
        sizeAlphabet = len(self.a)
        if n == 0:
            return s
        while n != 0:
            print(self.a[n % sizeAlphabet].getCharater())
            s.addChar(self.a[n % sizeAlphabet].getCharater())
            n = int(n / sizeAlphabet)
        #print(s)
