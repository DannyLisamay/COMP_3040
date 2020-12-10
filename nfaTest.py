import nfa
import testDFA_2

NFA_NoStrings = nfa.NFA_NoStrings()
NFA_Even_Length = nfa.NFA_Even_Length()
NFA_Odd_Length = nfa.NFA_Odd_Length()
NFA_N1 = nfa.NFA_N1()
NFA_N2 = nfa.NFA_N2()
NFA_N4 = nfa.NFA_N4()
NFA_ThreeFromEndIsOne = nfa.NFA_ThreeFromEndIsOne()
NFA_HasEps = nfa.NFA_HasEps()
NFA_OneBB = nfa.NFA_OneBB()

"""
#*******TASK #26 ************
#nfaTrace(NFA_Even, [], True, True)
#nfaTrace(NFA_Odd, [], False, True)

#NFA no strings
#Always false
print(nfa.oracle(NFA_NoStrings, [], False))
print(nfa.oracle(NFA_NoStrings, ["0", "0"], False))

#NFA Even length
print("NFA_Even_Length")
#True
print(nfa.oracle(NFA_Even_Length, [["q0"]], True))
print(nfa.oracle(NFA_Even_Length, [], True))
print(nfa.oracle(NFA_Even_Length, [["q1", "0"], ["q0", "1"]], True))
#False
print(nfa.oracle(NFA_Even_Length, [["q1", "0"]], False))
print(nfa.oracle(NFA_Even_Length, [["q1", "0"],["q0", "1"],["q1", "0"]], False))

#NFA Odd length
print("NFA_Odd_Length")
#True
print(nfa.oracle(NFA_Odd_Length, [["q1", "0"]], True))
print(nfa.oracle(NFA_Odd_Length, [["q1", "0"],["q0", "1"],["q1", "0"]], True))
#False
print(nfa.oracle(NFA_Odd_Length, [["q0"]], False))
print(nfa.oracle(NFA_Odd_Length, [], False))
print(nfa.oracle(NFA_Odd_Length, [["q1", "0"], ["q0", "1"]], False))

#NFA N1
print("NFA_N1")
#True
print(nfa.oracle(NFA_N1, [["q1" , "1"], ["q2", "0"], ["q3", "1"]], True))
print(nfa.oracle(NFA_N1, [["q1" , "1"], ["q2"], ["q3", "1"]], True))
print(nfa.oracle(NFA_N1, [["q1" , "1"], ["q2", "0"], ["q3", "1"], ["q3", "1"]], True))
#False
print(nfa.oracle(NFA_N1, [], False))
print(nfa.oracle(NFA_N1, [["q0" , "1"], ["q0", "0"], ["q0", "1"]], False))
print(nfa.oracle(NFA_N1, [["q1" , "1"],["q2", "0"]], False))


#NFA N2
print("NFA_N2")
#True
print(nfa.oracle(NFA_N2, [["q1", "1"], ["q2", "0"], ["q3", "1"]], True))
print(nfa.oracle(NFA_N2, [["q1", "1"], ["q2", "1"], ["q3", "0"]], True))
print(nfa.oracle(NFA_N2, [["q0", "1"], ["q1", "1"], ["q2", "0"], ["q3", "1"]], True))
#False
print(nfa.oracle(NFA_N2, [], False))
print(nfa.oracle(NFA_N2, [["q0", "1"], ["q0", "0"], ["q0", "1"]], False))
print(nfa.oracle(NFA_N2, [["q0", "1"],["q1", "1"]], False))

#NFA N4
print("NFA_N4")
#True
print(nfa.oracle(NFA_N4, [], True))
print(nfa.oracle(NFA_N4, [["q2"], ["q0", "a"]], True))
print(nfa.oracle(NFA_N4, [["q1", "b"], ["q2", "a"], ["q0", "a"]], True))
#False
print(nfa.oracle(NFA_N4, [["q1", "b"]], False))
print(nfa.oracle(NFA_N4, [["q1", "b"], ["q2", "a"]], False))
print(nfa.oracle(NFA_N4, [["q1", "b"], ["q1", "a"], ["q1", "a"]], False))

#NFA ThreeFromEndIsOne
print("NFA_ThreeFromEndIsOne")
print(nfa.oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["0", "1"], ["0", "0"], ["0", "1"]], False))
print(nfa.oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["0", "1"], ["0", "0"]], False))
print(nfa.oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["1", "1"], ["2", "1"], ["3", "1"]], True))
print(nfa.oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["1", "1"], ["2", "0"], ["3", "1"]], True))

#NFA HasEpsilon
print(nfa.oracle(NFA_HasEps, [] , False))
print(nfa.oracle(NFA_HasEps, [["1"]] , True))
print(nfa.oracle(NFA_HasEps, [["2"]] , False))
print(nfa.oracle(NFA_HasEps, [["0", "0"]] , False))
print(nfa.oracle(NFA_HasEps, [["0", "0"], ["1"]] , True))

"""

"""
#*******TASK #28 ************
# Define a data type to represent trace trees.
# True(accepts) || False(reject) || Branch [q, [tt ...]]
#*******TASK #29 ************
#For each example NFA, write a half-dozen trace trees of their behavior.
#NFA One Blah Blah
#[0, False]
print(nfa.forking(NFA_OneBB, []))
#[0, [0, False]
print(nfa.forking(NFA_OneBB, "0"))
#NFA N1
#[q0, False]
print(nfa.forking(NFA_N1, []))
#[q0, [q0, False]
print(nfa.forking(NFA_N1, "0"))
#[q0,[q1, False, [q0, False]]]
print(nfa.forking(NFA_N1, "1"))
#[q0,[q1, False, [q0, False]]]
print(nfa.forking(NFA_N1, "10"))
#[q0,[q1, False, [q0, False]]]
print(nfa.forking(NFA_N1, "101"))
"""
