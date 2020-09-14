#Danny Lisamay
#
#Test Class
import alphabet
import character

#Testing Alphabets
#empty alphabet
emptyAlphabet = alphabet.alphabet()
print(emptyAlphabet)
#binary alphabet
binary = [character.character("0"), character.character("1")]
binaryAlphabet = alphabet.alphabet(binary)
print(binaryAlphabet)
