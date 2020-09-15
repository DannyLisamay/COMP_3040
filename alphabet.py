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
        def insertChar(self, c):
            self.s.insert(0,c)
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
        s = self.strings(s = [])
        sizeAlphabet = len(self.a)
        exp = 0
        i = 0
        if n == 0:
            return s
        while True:
            if sizeAlphabet ** exp <= n:
                n -= sizeAlphabet ** exp
                exp += 1
            else:
                while i < exp:
                    s.insertChar(self.a[int(n % sizeAlphabet)])
                    n = int(n /sizeAlphabet)
                    i += 1
                return(s)
