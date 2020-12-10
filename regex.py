#*******TASK #41 ************
#Define a data type to represent regular expressions.
#Empty
class Regex_Empty:
    def __init__(self):
		pass
#Epsilon
class Regex_Epsilon:
    def __init__(self):
		pass
#Char
class Regex_Char:
    def __init__(self, c):
		self.c = c
#Union
class Regex_Union:
    def __init__(self, left, right):
		self.l = left
		self.r = right
#Star
class Regex_Star
    def __init__(self, x):
		self.x = x

#Circ
class Regex_Circ:
    def __init__(self, left, right):
		self.l = left
		self.r = right
