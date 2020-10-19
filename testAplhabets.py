#Danny Lisamay
#9/11
#Aplhabet Test Class
#9/14
import alphabet

#**Testing Alphabets
#***empty alphabet
emptyAlphabet = alphabet.Alphabet()
#print(emptyAlphabet)
#**binary alphabet
binary = [alphabet.Character("0"), alphabet.Character("1")]
binaryAlphabet = alphabet.Alphabet(binary)
#print(binaryAlphabet)
#**Pen Tablet alphabet
#penAndTablet = [character.character("Pen"), character.character("Tablet")]
#penAndTabletAlphabet = alphabet.alphabet(penAndTablet)
#print(penAndTabletAlphabet)

#**string Test
#strBinaryAlphabet = [binaryAlphabet.a[0], binaryAlphabet.a[0], binaryAlphabet.a[0], binaryAlphabet.a[1]]
#s = binaryAlphabet.strings(strBinaryAlphabet)
#print(s)

#**lexicographic test
print (emptyAlphabet.Lexicographic(1))
print (emptyAlphabet.Lexicographic(20))
print (emptyAlphabet.Lexicographic(2))
print (emptyAlphabet.Lexicographic(3))
print (emptyAlphabet.Lexicographic(5))
print (binaryAlphabet.Lexicographic(15))
