#Danny Lisamay
#9/11
#Aplhabet Test Class
#9/14
import alphabet
import character
import dfa

# Alphabets
#**empty
emptyAlphabet = alphabet.alphabet()
#**binary alphabet
binaryAlphabet = alphabet.alphabet([character.character("0"), character.character("1")])

# States
zeroState = ["0"]
abState = ["a","b"]

#DFA
#** dfa accepts no strings
#noStrings transitionFunction, kinda dumb function, always return first state
def acceptsNoStrings(s,c):
    dfaNoStrings.setState = s
dfaNoStrings = dfa.dfa(zeroState, binaryAlphabet , acceptsNoStrings , zeroState[0], ["0"])
#print(dfaNoStrings.isValid())

#** dfa accepts empty string
binaryAlphabetEmptyString = binaryAlphabet.strings([])
binaryAplhabetNonEmptyString = binaryAlphabet.strings([character.character("0"), character.character("1"),character.character("0"), character.character("1")])
#** this transitionFunction only works with abState [a,b]
#Parameters dfa, state, charater
def acceptsEmptyString(self, s, c):
    if type(c) == alphabet.alphabet.strings and c.isEmpty() :
        self.currentState = "b"
    else:
        self.currentState = "a"

dfaEmptyString = dfa.dfa(abState, binaryAlphabet, acceptsEmptyString, abState[0], ["b"])
dfaEmptyString.transition(dfaEmptyString, dfaEmptyString.currentState, binaryAlphabetEmptyString)
