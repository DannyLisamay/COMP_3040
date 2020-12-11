import nfa
import testDFA_2
import nfaTest
import dfa_ver2
import regex
NFA_NoStrings = nfa.NFA_NoStrings()
NFA_Even_Length = nfa.NFA_Even_Length()
NFA_Odd_Length = nfa.NFA_Odd_Length()
NFA_N1 = nfa.NFA_N1()
NFA_N2 = nfa.NFA_N2()
NFA_N4 = nfa.NFA_N4()
NFA_ThreeFromEndIsOne = nfa.NFA_ThreeFromEndIsOne()
NFA_HasEps = nfa.NFA_HasEps()
NFA_OneBB = nfa.NFA_OneBB()

DFA_NoStrings = nfa.nfa2dfa(NFA_NoStrings)
DFA_Even_Length = nfa.nfa2dfa(NFA_Even_Length)
DFA_Odd_Length = nfa.nfa2dfa(NFA_Odd_Length)
DFA_N1 = nfa.nfa2dfa(NFA_N1)
DFA_N2 = nfa.nfa2dfa(NFA_N2)
DFA_N4 = nfa.nfa2dfa(NFA_N4)
DFA_ThreeFromEndIsOne = nfa.nfa2dfa(NFA_ThreeFromEndIsOne)
DFA_HasEps = nfa.nfa2dfa(NFA_HasEps)
DFA_OneBB = nfa.nfa2dfa(NFA_OneBB)

nfa.backtrack(NFA_HasEps, [])
nfa.kleeneStar(NFA_NoStrings)
"""
#*******TASK #43 ************
#Write a example regular expressions.
#Basic regex
emptyR = regex.Regex_Empty()
#print(emptyR)
epsilonR = regex.Regex_Epsilon()
#print(epsilonR)

#Example from inclass
rbin = regex.Regex_Union(regex.Regex_Char(0), regex.Regex_Char(1))
ronebb = regex.Regex_Circ(regex.Regex_Star(rbin), regex.Regex_Circ(rbin,rbin))
#print(rbin)
#print(ronebb)

#Third from end is one
# Left Hand
#(0 U 1)
zeroUone = regex.Regex_Union(regex.Regex_Char(0),regex.Regex_Char(1))
#print(zeroUone)

#(0 U 1)*
starZeroUOne = regex.Regex_Star(zeroUone)
#print(starZeroUOne)

#Right Hand
#1
one = regex.Regex_Char(1)
#1(((0 U 1) C (0 U 1)))
rh = regex.Regex_Circ(one, regex.Regex_Union(zeroUone,zeroUone))
#print(rh)
#RE...
thirdFromEndIsOne = regex.Regex_Circ(starZeroUOne, rh)
#print(thirdFromEndIsOne)

#Example from textbook 1.56
a = regex.Regex_Char("a")
b = regex.Regex_Char("b")
ab = regex.Regex_Circ(a,b)
abUa = regex.Regex_Union(ab, a)
abUaStar = regex.Regex_Star(abUa)
#print(a)
#print(b)
#print(ab)
#print(abUa)
#print(abUaStar)


#*******TASK #43 ************
# Basic regex
#a
#pass
#a
#aa
#fail
#anything but a

#b
#pass
#b
#bbb
#fail
#anything but b

#ab should accept and b
#pass
#ab
#ab
#fail
#anything but ab

#abUa should accept a and b or a
#pass
#a
#ab
#ab
#aba
#abab
#fail
#any other letters or ending in two b
#abb

#thirdFromEndIsOne
#pass
#100
#0100
#111
#101
#fail
#000
#1
#0
#011


#*******generate tests ************
regex.generate(emptyR)
regex.generate(epsilonR)
regex.generate(a)
regex.generate(b)
regex.generate(ab)
regex.generate(abUaStar)
regex.generate(rbin)
regex.generate(ronebb)
regex.generate(thirdFromEndIsOne)
"""
