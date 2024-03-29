#Danny Lisamay
#9/11
#alphabet class
#alphabet is a list of characters
#character class
#some object with equality and printing
#9/13
#finished task 1 & 2
#created lexicographic function
#9/15
#finised task 3 lexicographic function


#********TASK #1************
#charater class
class Character:
    def __init__(self, c):
        self.c = c
    #set
    def setCharater(self, c):
        self.c = c
    #get
    def getCharater(self):
        return self.c
    #toString
    def __str__(self):
        return self.c

#********TASK #2************
#strings class
class Strings:
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

#alphabet class
class Alphabet:
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

    #********TASK #3************
    #generate Nth string lexicographic order
    def Lexicographic(self, n):
        s = Strings(s = [])
        sizeAlphabet = len(self.a)
        #exponent set to 0
        exp = 0
        i = 0
        #if string is empty or alphabet is empty return empty string
        if n == 0 or self.isEmpty():
            return s
        #loop until return
        while True:
            #which n ^ exp lexi is in.
            if sizeAlphabet ** exp <= n:
                n -= sizeAlphabet ** exp
                exp += 1
            else:
                while i < exp:
                    #professors example
                    s.insertChar(self.a[int(n % sizeAlphabet)])
                    n = int(n /sizeAlphabet)
                    i += 1
                return(s)
