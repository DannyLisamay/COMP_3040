import dfa
import alphabet

#Testing
#always False
#NoStringsDFA = dfa.DFA_NoStrings()
#print(NoStringsDFA.inAcceptState())

#transtions to q1
#dfaEmptyString = dfa.DFA_EmptyStrings()
#print(dfaEmptyString.getCurrentState())
#dfaEmptyString.transitionToState("")
#print(dfaEmptyString.getCurrentState())
#print(dfaEmptyString.inAcceptState())

#only take string of char
#dfaStringOfChar = dfa.DFA_StringOfChar("0")
#print(dfaStringOfChar.inAcceptState())
#dfaStringOfChar.transitionToState("0")
#print(dfaStringOfChar.inAcceptState())
#print(dfaStringOfChar.isStringAccepted("00100"))
#dfaStringOfChar.printTrace()


#********TASK #9************
dfaEven = dfa.DFA_Even()
#pass
#print(dfaEven.isStringAccepted("11"))
#print(dfaEven.isStringAccepted("00"))
#print(dfaEven.isStringAccepted("0101"))
#print(dfaEven.isStringAccepted("1010"))

#fail
#print(dfaEven.isStringAccepted("1"))
#print(dfaEven.isStringAccepted("0"))
#print(dfaEven.isStringAccepted("010"))
#print(dfaEven.isStringAccepted("101"))

#dfaEven.printTrace()

dfaOdd = dfa.DFA_Odd()
#pass
#print(dfaOdd.isStringAccepted("1"))
#print(dfaOdd.isStringAccepted("0"))
#print(dfaOdd.isStringAccepted("010"))
#print(dfaOdd.isStringAccepted("101"))

#fail
#print(dfaOdd.isStringAccepted("11"))
#print(dfaOdd.isStringAccepted("00"))
#print(dfaOdd.isStringAccepted("0101"))
#print(dfaOdd.isStringAccepted("1010"))

#dfaOdd.printTrace()

dfaM1 = dfa.DFA_M1()
#pass
#print(dfaM1.isStringAccepted("1"))
#print(dfaM1.isStringAccepted("11"))
#print(dfaM1.isStringAccepted("101"))
#print(dfaM1.isStringAccepted("1011"))

#fail
#print(dfaM1.isStringAccepted("0"))
#print(dfaM1.isStringAccepted("10"))
#print(dfaM1.isStringAccepted("00"))
#print(dfaM1.isStringAccepted("010"))
#dfaM1.printTrace()

dfaM2 = dfa.DFA_M2()
#pass
#print(dfaM2.isStringAccepted("1"))
#print(dfaM2.isStringAccepted("01"))
#print(dfaM2.isStringAccepted("11"))
#print(dfaM2.isStringAccepted("101"))

#fail
#print(dfaM2.isStringAccepted("0"))
#print(dfaM2.isStringAccepted("10"))
#print(dfaM2.isStringAccepted("100"))
#print(dfaM2.isStringAccepted("1010"))

#dfaM2.printTrace()

dfaM3 = dfa.DFA_M3()
#pass
#print(dfaM3.isStringAccepted("0"))
#print(dfaM3.isStringAccepted("10"))
#print(dfaM3.isStringAccepted("100"))
#print(dfaM3.isStringAccepted("1010"))

#fail
#print(dfaM3.isStringAccepted("1"))
#print(dfaM3.isStringAccepted("01"))
#print(dfaM3.isStringAccepted("11"))
#print(dfaM3.isStringAccepted("101"))

#dfaM3.printTrace()

dfaM4 = dfa.DFA_M4()
#Pass
#q
#print(dfaM4.isStringAccepted("a"))
#print(dfaM4.isStringAccepted("aa"))
#print(dfaM4.isStringAccepted("aba"))
#print(dfaM4.isStringAccepted("abaa"))
#r
#print(dfaM4.isStringAccepted("b"))
#print(dfaM4.isStringAccepted("bb"))
#print(dfaM4.isStringAccepted("bab"))
#print(dfaM4.isStringAccepted("babb"))

#fail
#q
#print(dfaM4.isStringAccepted("ab"))
#print(dfaM4.isStringAccepted("abb"))
#print(dfaM4.isStringAccepted("abab"))
#print(dfaM4.isStringAccepted("ababb"))
#r
#print(dfaM4.isStringAccepted("ba"))
#print(dfaM4.isStringAccepted("baa"))
#print(dfaM4.isStringAccepted("baba"))
#print(dfaM4.isStringAccepted("babaa"))

#dfaM4.printTrace()


dfaStrings001 = dfa.DFA_Strings001()
#Pass
#print(dfaStrings001.isStringAccepted("001"))
#print(dfaStrings001.isStringAccepted("00001"))
#print(dfaStrings001.isStringAccepted("00100"))
#print(dfaStrings001.isStringAccepted("0000"))

#Fail
#print(dfaStrings001.isStringAccepted("011111"))
#print(dfaStrings001.isStringAccepted("000000"))
#print(dfaStrings001.isStringAccepted("011"))
#print(dfaStrings001.isStringAccepted("0110"))

#dfa.printTrace();
