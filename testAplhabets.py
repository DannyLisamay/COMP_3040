#Danny Lisamay
#9/11
#Aplhabet Test Class
#9/14
import alphabet
import character

#**Testing Alphabets
#***empty alphabet
emptyAlphabet = alphabet.alphabet()
#print(emptyAlphabet)
#**binary alphabet
binary = [character.character("0"), character.character("1")]
binaryAlphabet = alphabet.alphabet(binary)
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
print (emptyAlphabet.lexicographic(7))
print (binaryAlphabet.lexicographic(15))
