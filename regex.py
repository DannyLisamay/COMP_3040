import random
#*******TASK #41 ************
#Define a data type to represent regular expressions.
#Objects

#*******TASK #42 ************
#Write a printer for regular expressions.
#toString format __str__

#*******TASK #45 ************
#Write a function that accepts a regular expressions and generates
#a random string that would be accepted by it.
#
#Empty
class Regex_Empty:
    def __init__(self):
        pass
    #toString format
    def __str__(self):
        return "Empty"
    #generate
    def generate(self):
        return []
#Epsilon
class Regex_Epsilon:
    def __init__(self):
        pass
    #toString format
    def __str__(self):
        return "Epsilon"
    #generate
    def generate(self):
        return None
#Char
class Regex_Char:
    def __init__(self, c):
        self.c = c
    #toString format
    def __str__(self):
        return str(self.c)
    #generate
    def generate(self):
        return [self.c]
#Union
class Regex_Union:
    def __init__(self, left, right):
        self.l = left
        self.r = right
    #toString format
    def __str__(self):
        return f"({self.l} U {self.r})"
    #generate
    def generate(self):
        return self.randomOr(self.l.generate(), self.r.generate())
    #randomOr used for union getnerate funtion
    def randomOr(self,l , r):
        # 50/50 chance
        coin = random.uniform(0, 1) <= .5
        if coin:
            [f, s] = [l, r]
        else:
            [f, s] = [r, l]
        if f:
            return f
        else:
            return s
#Star
class Regex_Star:
    def __init__(self, x):
        self.x = x
    #toString format
    def __str__(self):
        return f"({self.x} *"
    #generate
    def generate(self):
        # Temp objects, probably not the best way to do this but it works.
        eR = Regex_Empty()
        cR = Regex_Circ(self.x, self)
        uR = Regex_Union(eR, cR)
        return uR.generate()

class Regex_Circ:
    def __init__(self, left, right):
        self.l = left
        self.r = right
    #toString format
    def __str__(self):
        return f"({self.l} C {self.r})"
    #generate
    def generate(self):
        gl = self.l.generate()
        gr = self.r.generate()
        if gl and gr:
            return gl + gr
        else:
            return False

def generate(r):
    for x in range(10):
        print(r.generate())
