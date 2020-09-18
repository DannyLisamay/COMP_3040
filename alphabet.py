#Danny Lisamay
#9/11
#alphabet class
#alphabet is a list of characters
#9/13
#finished task 1 & 2
#created lexicographic function
#9/15
#finised task 3 lexicographic function

import character
class alphabet:
    #alphabet List
    def __init__(self, a = []):
        self.a = a
    #toString
    def __str__(self):
        #getCharater and format into a string
        #binary ex. [(0),(1)]
        strAlphabet = "Aplhabet = ["
        if len(self.a) != 0:
            for x in range(len(self.a)):
                strAlphabet += "(" + self.a[x].getCharater() + ")"
                if x != len(self.a) - 1:
                    strAlphabet += ","
        else:
            strAlphabet += '\u00D8'
        strAlphabet += "]"
        return strAlphabet
    #isEmpty
    def isEmpty(self):
        bool = False
        if len(self.a) == 0:
            bool = True
        return bool

    #strings class
    class strings:
        def __init__(self, s: list):
            self.s = s
        #insert character
        def insertChar(self, c):
            self.s.insert(0,c)
        #checks if emptyAlphabet
        def isEmpty(self):
            bool = False
            if len(self.s) == 0:
                bool = True
            return bool
        #toString format
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
        if n == 0 or self.isEmpty():
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
