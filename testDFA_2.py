import dfa_ver2
import alphabet

# Testing DFAs with memebership functions

dfaNoStrings = dfa_ver2.DFA_NoStrings()
print("**************")
print("DFA_NoStrings")
print(dfaNoStrings.isStringAccepted(""))
print(dfaNoStrings.trace(""))
print(dfaNoStrings.isStringAccepted("0000"))
print(dfaNoStrings.trace("0000"))


dfaEmptyString = dfa_ver2.DFA_EmptyStrings()
print("**************")
print("DFA_EmptyStrings")
#pass
print(dfaEmptyString.isStringAccepted(" "))
print(dfaEmptyString.trace(" "))
print(dfaEmptyString.isStringAccepted("   "))
print(dfaEmptyString.trace("   "))

#fail
print(dfaEmptyString.isStringAccepted("a "))
print(dfaEmptyString.trace("a "))
print(dfaEmptyString.isStringAccepted(" b "))
print(dfaEmptyString.trace(" b "))


dfaStringOfChar = dfa_ver2.DFA_StringOfChar("0")
print("**************")
print("DFA_StringOfChar")
#pass
print(dfaStringOfChar.isStringAccepted("0"))
print(dfaStringOfChar.trace("0"))
print(dfaStringOfChar.isStringAccepted("00"))
print(dfaStringOfChar.trace("00"))
print(dfaStringOfChar.isStringAccepted("000"))
print(dfaStringOfChar.trace("000"))
#fail
print(dfaStringOfChar.isStringAccepted(""))
print(dfaStringOfChar.trace(""))
print(dfaStringOfChar.isStringAccepted(" "))
print(dfaStringOfChar.trace(" "))
print(dfaStringOfChar.isStringAccepted(" a"))
print(dfaStringOfChar.trace(" a"))
print(dfaStringOfChar.isStringAccepted("as0a"))
print(dfaStringOfChar.trace("av0"))


dfaEven = dfa_ver2.DFA_Even()
print("**************")
print("DFA_Even")
#pass
print(dfaEven.isStringAccepted("11"))
print(dfaEven.trace("11"))
print(dfaEven.isStringAccepted("00"))
print(dfaEven.trace("00"))
print(dfaEven.isStringAccepted("0101"))
print(dfaEven.trace("0101"))
print(dfaEven.isStringAccepted("1010"))
print(dfaEven.trace("1010"))

#fail
print(dfaEven.isStringAccepted("1"))
print(dfaEven.trace("1"))
print(dfaEven.isStringAccepted("0"))
print(dfaEven.trace("0"))
print(dfaEven.isStringAccepted("010"))
print(dfaEven.trace("010"))
print(dfaEven.isStringAccepted("101"))
print(dfaEven.trace("101"))


dfaOdd = dfa_ver2.DFA_Odd()
print("**************")
print("DFA_Odd")
#pass
print(dfaOdd.isStringAccepted("1"))
print(dfaOdd.isStringAccepted("0"))
print(dfaOdd.isStringAccepted("010"))
print(dfaOdd.isStringAccepted("101"))
print(dfaOdd.trace("1"))
print(dfaOdd.trace("0"))
print(dfaOdd.trace("010"))
print(dfaOdd.trace("101"))

#fail
print(dfaOdd.isStringAccepted("11"))
print(dfaOdd.isStringAccepted("00"))
print(dfaOdd.isStringAccepted("0101"))
print(dfaOdd.isStringAccepted("1010"))
print(dfaOdd.trace("11"))
print(dfaOdd.trace("00"))
print(dfaOdd.trace("0101"))
print(dfaOdd.trace("1010"))

dfaM1 = dfa_ver2.DFA_M1()
print("**************")
print("DFA_M1")
#pass
print(dfaM1.isStringAccepted("1"))
print(dfaM1.isStringAccepted("11"))
print(dfaM1.isStringAccepted("101"))
print(dfaM1.isStringAccepted("1011"))
print(dfaM1.trace("1"))
print(dfaM1.trace("11"))
print(dfaM1.trace("101"))
print(dfaM1.trace("1011"))

#fail
print(dfaM1.isStringAccepted("0"))
print(dfaM1.isStringAccepted("10"))
print(dfaM1.isStringAccepted("00"))
print(dfaM1.isStringAccepted("010"))
print(dfaM1.trace("0"))
print(dfaM1.trace("10"))
print(dfaM1.trace("00"))
print(dfaM1.trace("010"))

dfaM2 = dfa_ver2.DFA_M2()
print("**************")
print("DFA_M2")
#pass
print(dfaM2.isStringAccepted("1"))
print(dfaM2.isStringAccepted("01"))
print(dfaM2.isStringAccepted("11"))
print(dfaM2.isStringAccepted("101"))
print(dfaM2.trace("1"))
print(dfaM2.trace("01"))
print(dfaM2.trace("11"))
print(dfaM2.trace("101"))

#fail
print(dfaM2.isStringAccepted("0"))
print(dfaM2.isStringAccepted("10"))
print(dfaM2.isStringAccepted("100"))
print(dfaM2.isStringAccepted("1010"))
print(dfaM2.trace("0"))
print(dfaM2.trace("10"))
print(dfaM2.trace("100"))
print(dfaM2.trace("1010"))

dfaM3 = dfa_ver2.DFA_M3()
print("**************")
print("DFA_M3")
#pass
print(dfaM3.isStringAccepted("0"))
print(dfaM3.isStringAccepted("10"))
print(dfaM3.isStringAccepted("100"))
print(dfaM3.isStringAccepted("1010"))
print(dfaM3.trace("0"))
print(dfaM3.trace("10"))
print(dfaM3.trace("100"))
print(dfaM3.trace("1010"))

#fail
print(dfaM3.isStringAccepted("1"))
print(dfaM3.isStringAccepted("01"))
print(dfaM3.isStringAccepted("11"))
print(dfaM3.isStringAccepted("101"))
print(dfaM3.trace("1"))
print(dfaM3.trace("01"))
print(dfaM3.trace("11"))
print(dfaM3.trace("101"))

dfaM4 = dfa_ver2.DFA_M4()
print("**************")
print("DFA_M4")
#Pass
#q
print(dfaM4.isStringAccepted("a"))
print(dfaM4.isStringAccepted("aa"))
print(dfaM4.isStringAccepted("aba"))
print(dfaM4.isStringAccepted("abaa"))
print(dfaM4.trace("a"))
print(dfaM4.trace("aa"))
print(dfaM4.trace("aba"))
print(dfaM4.trace("abaa"))
#r
print(dfaM4.isStringAccepted("b"))
print(dfaM4.isStringAccepted("bb"))
print(dfaM4.isStringAccepted("bab"))
print(dfaM4.isStringAccepted("babb"))
print(dfaM4.trace("b"))
print(dfaM4.trace("bb"))
print(dfaM4.trace("bab"))
print(dfaM4.trace("babb"))

#fail
#q
print(dfaM4.isStringAccepted("ab"))
print(dfaM4.isStringAccepted("abb"))
print(dfaM4.isStringAccepted("abab"))
print(dfaM4.isStringAccepted("ababb"))
print(dfaM4.trace("ab"))
print(dfaM4.trace("abb"))
print(dfaM4.trace("abab"))
print(dfaM4.trace("ababb"))
#r
print(dfaM4.isStringAccepted("ba"))
print(dfaM4.isStringAccepted("baa"))
print(dfaM4.isStringAccepted("baba"))
print(dfaM4.isStringAccepted("babaa"))
print(dfaM4.trace("ba"))
print(dfaM4.trace("baa"))
print(dfaM4.trace("baba"))
print(dfaM4.trace("babaa"))

dfaStrings001 = dfa_ver2.DFA_Strings001()
print("**************")
print("DFA_Strings001")
#Pass
print(dfaStrings001.isStringAccepted("001"))
print(dfaStrings001.isStringAccepted("00001"))
print(dfaStrings001.isStringAccepted("00100"))
print(dfaStrings001.isStringAccepted("00001"))
print(dfaStrings001.trace("001"))
print(dfaStrings001.trace("00001"))
print(dfaStrings001.trace("00100"))
print(dfaStrings001.trace("00001"))

#Fail
print(dfaStrings001.isStringAccepted("011111"))
print(dfaStrings001.isStringAccepted("000000"))
print(dfaStrings001.isStringAccepted("011"))
print(dfaStrings001.isStringAccepted("0110"))
print(dfaStrings001.trace("011111"))
print(dfaStrings001.trace("000000"))
print(dfaStrings001.trace("011"))
print(dfaStrings001.trace("0110"))


"""
#*******TASK #12 Test************
#print(dfaNoStrings.getAcceptedString());
#print(dfaEmptyString.getAcceptedString());
#print(dfaStringOfChar.getAcceptedString());
#print(dfaEven.getAcceptedString());
#print(dfaOdd.getAcceptedString());
#print(dfaM1.getAcceptedString());
#print(dfaM2.getAcceptedString());
#print(dfaM3.getAcceptedString());
#print(dfaM4.getAcceptedString());
#print(dfaStrings001.getAcceptedString());

#*******TASK #13 Test************
# Same test from 9/10, expected complement results.

#complement_dfaNoStrings = dfaNoStrings.complement()
#print(complement_dfaNoStrings.acceptStates)
#print(complement_dfaNoStrings.isStringAccepted(""))
#print(complement_dfaNoStrings.trace(""))
#print(complement_dfaNoStrings.isStringAccepted("0000"))
#print(complement_dfaNoStrings.trace("0000"))

#complement_dfaEmptyString = dfaEmptyString.complement()
#fail
#print(complement_dfaEmptyString.isStringAccepted(" "))
#print(complement_dfaEmptyString.trace(" "))
#print(complement_dfaEmptyString.isStringAccepted("   "))
#print(complement_dfaEmptyString.trace("   "))

#pass
#print(complement_dfaEmptyString.isStringAccepted("a "))
#print(complement_dfaEmptyString.trace("b "))
#print(complement_dfaEmptyString.isStringAccepted(" a "))
#print(complement_dfaEmptyString.trace(" b "))

#complement_dfaStringOfChar = dfaStringOfChar.complement()
#fail
#print(complement_dfaStringOfChar.isStringAccepted("0"))
#print(complement_dfaStringOfChar.trace("0"))
#print(complement_dfaStringOfChar.isStringAccepted("00"))
#print(complement_dfaStringOfChar.trace("00"))
#print(complement_dfaStringOfChar.isStringAccepted("000"))
#print(complement_dfaStringOfChar.trace("000"))
#fail
#print(complement_dfaStringOfChar.isStringAccepted(""))
#print(complement_dfaStringOfChar.trace(""))
#print(complement_dfaStringOfChar.isStringAccepted(" "))
#print(complement_dfaStringOfChar.trace(" "))
#print(complement_dfaStringOfChar.isStringAccepted(" a"))
#print(complement_dfaStringOfChar.trace(" a"))
#print(complement_dfaStringOfChar.isStringAccepted("as0a"))
#print(complement_dfaStringOfChar.trace("av0"))

complement_dfaEven = dfaEven.complement()
#fail
#print(complement_dfaEven.isStringAccepted("11"))
#print(complement_dfaEven.trace("11"))
#print(complement_dfaEven.isStringAccepted("00"))
#print(complement_dfaEven.trace("00"))
#print(complement_dfaEven.isStringAccepted("0101"))
#print(complement_dfaEven.trace("0101"))
#print(complement_dfaEven.isStringAccepted("1010"))
#print(complement_dfaEven.trace("1010"))

#pass
#print(complement_dfaEven.isStringAccepted("1"))
#print(complement_dfaEven.trace("1"))
#print(complement_dfaEven.isStringAccepted("0"))
#print(complement_dfaEven.trace("0"))
#print(complement_dfaEven.isStringAccepted("010"))
#print(complement_dfaEven.trace("010"))
#print(complement_dfaEven.isStringAccepted("101"))
#print(complement_dfaEven.trace("101"))

complement_dfaOdd = dfaOdd.complement()
#fail
#print(complement_dfaOdd.isStringAccepted("1"))
#print(complement_dfaOdd.isStringAccepted("0"))
#print(complement_dfaOdd.isStringAccepted("010"))
#print(complement_dfaOdd.isStringAccepted("101"))
#print(complement_dfaOdd.trace("1"))
#print(complement_dfaOdd.trace("0"))
#print(complement_dfaOdd.trace("010"))
#print(complement_dfaOdd.trace("101"))

#pass
#print(complement_dfaOdd.isStringAccepted("11"))
#print(complement_dfaOdd.isStringAccepted("00"))
#print(complement_dfaOdd.isStringAccepted("0101"))
#print(complement_dfaOdd.isStringAccepted("1010"))
#print(complement_dfaOdd.trace("11"))
#print(complement_dfaOdd.trace("00"))
#print(complement_dfaOdd.trace("0101"))
#print(complement_dfaOdd.trace("1010"))

complement_dfaM1 = dfaM1.complement()
#fail
#print(complement_dfaM1.isStringAccepted("1"))
#print(complement_dfaM1.isStringAccepted("11"))
#print(complement_dfaM1.isStringAccepted("101"))
#print(complement_dfaM1.isStringAccepted("1011"))
#print(complement_dfaM1.trace("1"))
#print(complement_dfaM1.trace("11"))
#print(complement_dfaM1.trace("101"))
#print(complement_dfaM1.trace("1011"))

#pass
#print(complement_dfaM1.isStringAccepted("0"))
#print(complement_dfaM1.isStringAccepted("10"))
#print(complement_dfaM1.isStringAccepted("00"))
#print(complement_dfaM1.isStringAccepted("010"))
#print(complement_dfaM1.trace("0"))
#print(complement_dfaM1.trace("10"))
#print(complement_dfaM1.trace("00"))
#print(complement_dfaM1.trace("010"))

complement_dfaM2 = dfaM2.complement()
#fail
#print(complement_dfaM2.isStringAccepted("1"))
#print(complement_dfaM2.isStringAccepted("01"))
#print(complement_dfaM2.isStringAccepted("11"))
#print(complement_dfaM2.isStringAccepted("101"))
#print(complement_dfaM2.trace("1"))
#print(complement_dfaM2.trace("01"))
#print(complement_dfaM2.trace("11"))
#print(complement_dfaM2.trace("101"))

#pass
#print(complement_dfaM2.isStringAccepted("0"))
#print(complement_dfaM2.isStringAccepted("10"))
#print(complement_dfaM2.isStringAccepted("100"))
#print(complement_dfaM2.isStringAccepted("1010"))
#print(complement_dfaM2.trace("0"))
#print(complement_dfaM2.trace("10"))
#print(complement_dfaM2.trace("100"))
#print(complement_dfaM2.trace("1010"))

complement_dfaM3 = dfaM3.complement()
#fail
#print(complement_dfaM3.isStringAccepted("0"))
#print(complement_dfaM3.isStringAccepted("10"))
#print(complement_dfaM3.isStringAccepted("100"))
#print(complement_dfaM3.isStringAccepted("1010"))
#print(complement_dfaM3.trace("0"))
#print(complement_dfaM3.trace("10"))
#print(complement_dfaM3.trace("100"))
#print(complement_dfaM3.trace("1010"))

#pass
#print(complement_dfaM3.isStringAccepted("1"))
#print(complement_dfaM3.isStringAccepted("01"))
#print(complement_dfaM3.isStringAccepted("11"))
#print(complement_dfaM3.isStringAccepted("101"))
#print(complement_dfaM3.trace("1"))
#print(complement_dfaM3.trace("01"))
#print(complement_dfaM3.trace("11"))
#print(complement_dfaM3.trace("101"))

complement_dfaM4 = dfaM4.complement()
#Fail
#q
#print(complement_dfaM4.isStringAccepted("a"))
#print(complement_dfaM4.isStringAccepted("aa"))
#print(complement_dfaM4.isStringAccepted("aba"))
#print(complement_dfaM4.isStringAccepted("abaa"))
#print(complement_dfaM4.trace("a"))
#print(complement_dfaM4.trace("aa"))
#print(complement_dfaM4.trace("aba"))
#print(complement_dfaM4.trace("abaa"))
#r
#print(complement_dfaM4.isStringAccepted("b"))
#print(complement_dfaM4.isStringAccepted("bb"))
#print(complement_dfaM4.isStringAccepted("bab"))
#print(complement_dfaM4.isStringAccepted("babb"))
#print(complement_dfaM4.trace("b"))
#print(complement_dfaM4.trace("bb"))
#print(complement_dfaM4.trace("bab"))
#print(complement_dfaM4.trace("babb"))

#Pass
#q
#print(complement_dfaM4.isStringAccepted("ab"))
#print(complement_dfaM4.isStringAccepted("abb"))
#print(complement_dfaM4.isStringAccepted("abab"))
#print(complement_dfaM4.isStringAccepted("ababb"))
#print(complement_dfaM4.trace("ab"))
#print(complement_dfaM4.trace("abb"))
#print(complement_dfaM4.trace("abab"))
#print(complement_dfaM4.trace("ababb"))
#r
#print(complement_dfaM4.isStringAccepted("ba"))
#print(complement_dfaM4.isStringAccepted("baa"))
#print(complement_dfaM4.isStringAccepted("baba"))
#print(complement_dfaM4.isStringAccepted("babaa"))
#print(complement_dfaM4.trace("ba"))
#print(complement_dfaM4.trace("baa"))
#print(complement_dfaM4.trace("baba"))
#print(complement_dfaM4.trace("babaa"))

complement_dfaStrings001 = dfaStrings001.complement()
#Fail
#print(complement_dfaStrings001.isStringAccepted("001"))
#print(complement_dfaStrings001.isStringAccepted("00001"))
#print(complement_dfaStrings001.isStringAccepted("00100"))
#print(complement_dfaStrings001.isStringAccepted("00001"))
#print(complement_dfaStrings001.trace("001"))
#print(complement_dfaStrings001.trace("00001"))
#print(complement_dfaStrings001.trace("00100"))
#print(complement_dfaStrings001.trace("00001"))

#Pass
#print(complement_dfaStrings001.isStringAccepted("011111"))
#print(complement_dfaStrings001.isStringAccepted("000000"))
#print(complement_dfaStrings001.isStringAccepted("011"))
#print(complement_dfaStrings001.isStringAccepted("0110"))
#print(complement_dfaStrings001.trace("011111"))
#print(complement_dfaStrings001.trace("000000"))
#print(complement_dfaStrings001.trace("011"))
#print(complement_dfaStrings001.trace("0110"))


#*******TASK #14 Test************
listA = ["0","1"]
listB = ["0","1","2"]
print(list(set(listB) - set(listA)))
#*******TASK #15 ************
"""
