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
#********Task #11 Tests*****
dfaNoStrings = dfa.DFA_NoStrings()
#print(dfaNoStrings.isStringAccepted(""))
#print(dfaNoStrings.trace(""))
#print(dfaNoStrings.isStringAccepted("0000"))
#print(dfaNoStrings.trace("0000"))

dfaEmptyString = dfa.DFA_EmptyStrings()
#pass
#print(dfaEmptyString.isStringAccepted(" "))
#print(dfaEmptyString.trace(" "))
#print(dfaEmptyString.isStringAccepted("   "))
#print(dfaEmptyString.trace("   "))

#fail
#print(dfaEmptyString.isStringAccepted("a "))
#print(dfaEmptyString.trace("b "))
#print(dfaEmptyString.isStringAccepted(" a "))
#print(dfaEmptyString.trace(" b "))

dfaStringOfChar = dfa.DFA_StringOfChar("0")
#pass
#print(dfaStringOfChar.isStringAccepted("0"))
#print(dfaStringOfChar.trace("0"))
#print(dfaStringOfChar.isStringAccepted("00"))
#print(dfaStringOfChar.trace("00"))
#print(dfaStringOfChar.isStringAccepted("000"))
#print(dfaStringOfChar.trace("000"))
#fail
#print(dfaStringOfChar.isStringAccepted(""))
#print(dfaStringOfChar.trace(""))
#print(dfaStringOfChar.isStringAccepted(" "))
#print(dfaStringOfChar.trace(" "))
#print(dfaStringOfChar.isStringAccepted(" a"))
#print(dfaStringOfChar.trace(" a"))
#print(dfaStringOfChar.isStringAccepted("as0a"))
#print(dfaStringOfChar.trace("av0"))

dfaEven = dfa.DFA_Even()
#pass
#print(dfaEven.isStringAccepted("11"))
#print(dfaEven.trace("11"))
#print(dfaEven.isStringAccepted("00"))
#print(dfaEven.trace("00"))
#print(dfaEven.isStringAccepted("0101"))
#print(dfaEven.trace("0101"))
#print(dfaEven.isStringAccepted("1010"))
#print(dfaEven.trace("1010"))

#fail
#print(dfaEven.isStringAccepted("1"))
#print(dfaEven.trace("1"))
#print(dfaEven.isStringAccepted("0"))
#print(dfaEven.trace("0"))
#print(dfaEven.isStringAccepted("010"))
#print(dfaEven.trace("010"))
#print(dfaEven.isStringAccepted("101"))
#print(dfaEven.trace("101"))

dfaOdd = dfa.DFA_Odd()
#pass
#print(dfaOdd.isStringAccepted("1"))
#print(dfaOdd.isStringAccepted("0"))
#print(dfaOdd.isStringAccepted("010"))
#print(dfaOdd.isStringAccepted("101"))
#print(dfaOdd.trace("1"))
#print(dfaOdd.trace("0"))
#print(dfaOdd.trace("010"))
#print(dfaOdd.trace("101"))

#fail
#print(dfaOdd.isStringAccepted("11"))
#print(dfaOdd.isStringAccepted("00"))
#print(dfaOdd.isStringAccepted("0101"))
#print(dfaOdd.isStringAccepted("1010"))
#print(dfaOdd.trace("11"))
#print(dfaOdd.trace("00"))
#print(dfaOdd.trace("0101"))
#print(dfaOdd.trace("1010"))

dfaM1 = dfa.DFA_M1()
#pass
#print(dfaM1.isStringAccepted("1"))
#print(dfaM1.isStringAccepted("11"))
#print(dfaM1.isStringAccepted("101"))
#print(dfaM1.isStringAccepted("1011"))
#print(dfaM1.trace("1"))
#print(dfaM1.trace("11"))
#print(dfaM1.trace("101"))
#print(dfaM1.trace("1011"))

#fail
#print(dfaM1.isStringAccepted("0"))
#print(dfaM1.isStringAccepted("10"))
#print(dfaM1.isStringAccepted("00"))
#print(dfaM1.isStringAccepted("010"))
#print(dfaM1.trace("0"))
#print(dfaM1.trace("10"))
#print(dfaM1.trace("00"))
#print(dfaM1.trace("010"))

dfaM2 = dfa.DFA_M2()
#pass
#print(dfaM2.isStringAccepted("1"))
#print(dfaM2.isStringAccepted("01"))
#print(dfaM2.isStringAccepted("11"))
#print(dfaM2.isStringAccepted("101"))
#print(dfaM2.trace("1"))
#3print(dfaM2.trace("01"))
#print(dfaM2.trace("11"))
#print(dfaM2.trace("101"))

#fail
#print(dfaM2.isStringAccepted("0"))
#print(dfaM2.isStringAccepted("10"))
#print(dfaM2.isStringAccepted("100"))
#print(dfaM2.isStringAccepted("1010"))
#print(dfaM2.trace("0"))
#print(dfaM2.trace("10"))
#print(dfaM2.trace("100"))
#print(dfaM2.trace("1010"))

dfaM3 = dfa.DFA_M3()
#pass
#print(dfaM3.isStringAccepted("0"))
#print(dfaM3.isStringAccepted("10"))
#print(dfaM3.isStringAccepted("100"))
#print(dfaM3.isStringAccepted("1010"))
#print(dfaM3.trace("0"))
#print(dfaM3.trace("10"))
#print(dfaM3.trace("100"))
#print(dfaM3.trace("1010"))

#fail
#print(dfaM3.isStringAccepted("1"))
#print(dfaM3.isStringAccepted("01"))
#print(dfaM3.isStringAccepted("11"))
#print(dfaM3.isStringAccepted("101"))
#print(dfaM3.trace("1"))
#print(dfaM3.trace("01"))
#print(dfaM3.trace("11"))
#print(dfaM3.trace("101"))

dfaM4 = dfa.DFA_M4()
#Pass
#q
#print(dfaM4.isStringAccepted("a"))
#print(dfaM4.isStringAccepted("aa"))
#print(dfaM4.isStringAccepted("aba"))
#print(dfaM4.isStringAccepted("abaa"))
#print(dfaM4.trace("a"))
#print(dfaM4.trace("aa"))
#print(dfaM4.trace("aba"))
#print(dfaM4.trace("abaa"))
#r
#print(dfaM4.isStringAccepted("b"))
#print(dfaM4.isStringAccepted("bb"))
#print(dfaM4.isStringAccepted("bab"))
#print(dfaM4.isStringAccepted("babb"))
#print(dfaM4.trace("b"))
#print(dfaM4.trace("bb"))
#print(dfaM4.trace("bab"))
#print(dfaM4.trace("babb"))

#fail
#q
#print(dfaM4.isStringAccepted("ab"))
#print(dfaM4.isStringAccepted("abb"))
#print(dfaM4.isStringAccepted("abab"))
#print(dfaM4.isStringAccepted("ababb"))
#print(dfaM4.trace("ab"))
#print(dfaM4.trace("abb"))
#print(dfaM4.trace("abab"))
#print(dfaM4.trace("ababb"))
#r
#print(dfaM4.isStringAccepted("ba"))
#print(dfaM4.isStringAccepted("baa"))
#print(dfaM4.isStringAccepted("baba"))
#print(dfaM4.isStringAccepted("babaa"))
#print(dfaM4.trace("ba"))
#print(dfaM4.trace("baa"))
#print(dfaM4.trace("baba"))
#print(dfaM4.trace("babaa"))

dfaStrings001 = dfa.DFA_Strings001()
#Pass
#print(dfaStrings001.isStringAccepted("001"))
#print(dfaStrings001.isStringAccepted("00001"))
#print(dfaStrings001.isStringAccepted("00100"))
#print(dfaStrings001.isStringAccepted("00001"))
#print(dfaStrings001.trace("001"))
#print(dfaStrings001.trace("00001"))
#print(dfaStrings001.trace("00100"))
#print(dfaStrings001.trace("00001"))

#Fail
#print(dfaStrings001.isStringAccepted("011111"))
#print(dfaStrings001.isStringAccepted("000000"))
#print(dfaStrings001.isStringAccepted("011"))
#print(dfaStrings001.isStringAccepted("0110"))
#print(dfaStrings001.trace("011111"))
#print(dfaStrings001.trace("000000"))
#print(dfaStrings001.trace("011"))
#print(dfaStrings001.trace("0110"))
