#*******TASK #41 ************
#Define a data type to represent regular expressions.
#Objects
#*******TASK #42 ************
#Write a printer for regular expressions.
#toString format __str__
#Empty
class Regex_Empty:
    def __init__(self):
        pass
    #toString format
    def __str__(self):
        return "Empty "
#Epsilon
class Regex_Epsilon:
    def __init__(self):
        pass
    #toString format
    def __str__(self):
        return "Epsilon "
#Char
class Regex_Char:
    def __init__(self, c):
        self.c = c
    #toString format
    def __str__(self):
        return str(self.c)
#Union
class Regex_Union:
    def __init__(self, left, right):
        self.l = left
        self.r = right
    #toString format
    def __str__(self):
        return f"({self.l} U {self.r})"
#Star
class Regex_Star:
    def __init__(self, x):
        self.x = x
    #toString format
    def __str__(self):
        return f"({self.x} *"

#Circ
class Regex_Circ:
    def __init__(self, left, right):
        self.l = left
        self.r = right
    #toString format
    def __str__(self):
        return f"({self.l} C {self.r})"

#*******TASK #45 ************
#Write a function that accepts a regular expressions and generates
#a random string that would be accepted by it.
def generator(r):
    return []
