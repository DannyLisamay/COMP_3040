#Danny Lisamay
import alphabet
import dfa

# Alphabets
#**empty alphabet
emptyAlphabet = alphabet.Alphabet()
#**binary alphabet
binaryAlphabet = alphabet.Alphabet([alphabet.Character("0"), alphabet.Character("1")])

# States
zeroState = ["0"]
abState = ["a","b"]

#DFA
#*******TASK #5************
#** dfa accepts no strings
#noStrings transitionFunction, kinda dumb function, always return first state
def acceptsNoStrings(s,c):
    dfaNoStrings.setState = s
dfaNoStrings = dfa.dfa(zeroState, binaryAlphabet , acceptsNoStrings , zeroState[0], ["0"])
print(dfaNoStrings.isValid())

#********TASK #6************
#** dfa accepts empty string
binaryAlphabetEmptyString = binaryAlphabet.strings([])
binaryAplhabetNonEmptyString = binaryAlphabet.strings([character.character("0"), character.character("1"),character.character("0"), character.character("1")])
#** this transitionFunction only works with abState [a,b]
#Parameters dfa, state, charater
def acceptsEmptyString(self, s, c):
    if type(c) == alphabet.alphabet.strings and c.isEmpty():
        self.currentState = "b"
    else:
        self.currentState = "a"

dfaEmptyString = dfa.dfa(abState, binaryAlphabet, acceptsEmptyString, abState[0], ["b"])
dfaEmptyString.transition(dfaEmptyString, dfaEmptyString.currentState, binaryAlphabetEmptyString)
print(dfaEmptyString.isValid())

#********TASK #7************
#def dfaAcceptsStringsOfChar(self, c):
#    if type(c) != charater.charater:
#        print("c is not type charater")
#        return
#    return dfa.dfa(abState, binaryAlphabet, , abState[0], ["b"])
