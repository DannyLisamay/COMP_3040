#Danny Lisamay
#9/11
#character class
#some object with equality and printing

class character:
    c = ""
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
