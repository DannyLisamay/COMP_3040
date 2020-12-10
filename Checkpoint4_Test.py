import nfa
import testDFA_2
import nfaTest
import dfa_ver2

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
