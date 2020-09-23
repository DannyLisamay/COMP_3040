import dfa
import alphabet
#Testing
#always False
NoStringsDFA = dfa.DFA_NoStrings()
print(NoStringsDFA.inAcceptState())

#transtions to q1
dfaEmptyString = dfa.DFA_EmptyStrings()
print(dfaEmptyString.getCurrentState())
dfaEmptyString.transitionToState("")
print(dfaEmptyString.getCurrentState())
print(dfaEmptyString.inAcceptState())

#only take string of char
dfaStringOfChar = dfa.DFA_StringOfChar("0")
#print(dfaStringOfChar.inAcceptState())
#dfaStringOfChar.transitionToState("0")
#print(dfaStringOfChar.inAcceptState())
print(dfaStringOfChar.isStringAccepted("00100"))

dfaStringOfChar.printTrace()
