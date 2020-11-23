import nfa
import testDFA_2

NFA_NoStrings = nfa.NFA_NoStrings()
#NFA_Even
#NFA_Odd
NFA_Even_Length = nfa.NFA_Even_Length()
NFA_Odd_Length = nfa.NFA_Odd_Length()
NFA_N1 = nfa.NFA_N1()
NFA_N2 = nfa.NFA_N2()
NFA_N4 = nfa.NFA_N4()
NFA_ThreeFromEndIsOne = nfa.NFA_ThreeFromEndIsOne()

#*******TASK #26 ************
#nfaTrace(NFA_Even, [], True, True)
#nfaTrace(NFA_Odd, [], False, True)

#NFA no strings
#Always false
oracle(NFA_NoStrings, [], False)
oracle(NFA_NoStrings, ["0", "0"], False)

#NFA Even length
Print("NFA_Even_Length")
#True
oracle(NFA_Even_Length, ["q0", None], True)
oracle(NFA_Even_Length, [], True)
oracle(NFA_Even_Length, [["q1", "0"], ["q0", "1"]], True)
#False
oracle(NFA_Even_Length, [["q1", "0"]], False)
oracle(NFA_Even_Length, [["q1", "0"],["q0", "1"],["q1", "0"]], False)

#NFA Odd length
Print("NFA_Odd_Length")
#True
oracle(NFA_Odd_Length, [["q1", "0"]], True)
oracle(NFA_Odd_Length, [["q1", "0"],["q0", "1"],["q1", "0"]], True)
#False
oracle(NFA_Odd_Length, [["q0", None]], False)
oracle(NFA_Odd_Length, [], False)
oracle(NFA_Odd_Length, [["q1", "0"], ["q0", "1"]], False)

#NFA N1
Print("NFA_N1")
#True
oracle(NFA_N1, [["q1", "1"], ["q2", "0"], ["q3", "1"]], True)
oracle(NFA_N1, [["q1", "1"], ["q2", None], ["q3", "1"]], True)
oracle(NFA_N1, [["q1", "1"], ["q2", "0"], ["q3", "1"], ["q3", "1"]], True)
#False
oracle(NFA_N1, [], False)
oracle(NFA_N1, [["q0", "1"], ["q0", "0"], ["q0", "1"]], False)
oracle(NFA_N1, [["q1", "1"],["q2", "0"]], False)

#NFA N2
Print("NFA_N2")
#True
oracle(NFA_N2, [["q1", "1"], ["q2", "0"], ["q3", "1"]], True)
oracle(NFA_N2, [["q1", "1"], ["q2", "1"], ["q3", "0"]], True)
oracle(NFA_N2, [["q0", "1"], ["q1", "1"], ["q2", "0"], ["q3", "1"]], True)
#False
oracle(NFA_N2, [], False)
oracle(NFA_N2, [["q0", "1"], ["q0", "0"], ["q0", "1"]], False)
oracle(NFA_N2, [["q0", "1"],["q1", "1"]], False)

#NFA N4
Print("NFA_N4")
#True
oracle(NFA_N4, [], True)
oracle(NFA_N4, [["q2", None], ["q0", "a"]], True)
oracle(NFA_N4, [["q1", "b"], ["q2", "a"], ["q0", "a"]], True)
#False
oracle(NFA_N4, [["q1", "b"]], False)
oracle(NFA_N4, [["q1", "b"], ["q2", "a"]], False)
oracle(NFA_N4, [["q1", "b"], ["q1", "a"], ["q1", "a"]], False)

#NFA ThreeFromEndIsOne
Print("NFA_ThreeFromEndIsOne")
oracle(NFA_ThreeFromEndIsOne, [["1", "0"], ["0", "1"], ["0", "1"], ["0", "0"], ["0", "1"]], False)
oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["0", "1"], ["0", "0"], ["0", "1"]], True)
oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["1", "1"], ["2", "0"], ["2", "1"]], True)
oracle(NFA_ThreeFromEndIsOne, [["0", "0"], ["0", "1"], ["1", "1"], ["2", "0"], ["2", "1"]], False)
