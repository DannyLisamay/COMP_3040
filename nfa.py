import dfa_ver2

#*******TASK #23 ************
# Define a data type to represent NFAs.
class NFA:
    def __init__(self, statesFunction, alphabet, startState, transitionFunction, acceptFunction, epsilonFunction):
        self.statesFunction = statesFunction
        self.alpha = alphabet
        self.startState = startState
        self.transitionFunction = transitionFunction
        self.acceptFunction = acceptFunction
        self.epsilonFunction = epsilonFunction


#*******TASK #24 ************
# Write a (trivial) function that converts DFAs into NFAs.
# Pretty much what was gone over in class.
def dfa2Nfa(dfa):
    def transitionFunction(qi, c):
        return [dfa.transitionFunction]
    def epsilonFunction(qi):
        return []
    return DFA(dfa.statesFunction, dfa.alpha, dfa.startState, transitionFunction, dfa.acceptFunction, epsilonFunction)


#*******TASK #27 ************
#Write a function that given an NFA, a string, a trace, and a boolean,
#determines if the trace is a valid execution of the NFA and accepts results in the given boolean.

def oracle(nfa, trace, result):
    return oracle_(nfa, nfa.startState, trace, result)

#Helper function
def oracle_(nfa, qi, trace, result):
    # Check if trace is empty
    if not trace:
        return result == nfa.acceptFunction(qi)
    # te is first element tp is rest
    [te, *tp] = trace
    def qjs():
        # check if te is epsilon
        if len(te) == 1:
            return nfa.epsilonFunction(qi)
        # else transition
        else:
            return nfa.transitionFunction(qi, te[1])
    # Recursion
    print(qi)
    return te[0] in qjs() and oracle_(nfa, te[0], tp, result)
#*******TASK #25 ************
# Write a example NFAs.
# casted to tuple to work with my getAcceptedString function. (was an issue with DFAs)

# NFA NoStrings
# Doesn't accept anything always return false.
def NFA_NoStrings():
    return NFA(
        lambda x: x == "0",
        ["0", "1"],
        "0",
        lambda qi, c: "0",
        lambda qi: False,
        lambda qi: "0"
    )
#** dfa accepts even string length
def NFA_Even_Length():
    def transitionFunction(qi, c):
        if qi == "q0":
            return ["q1"]
        else:
            return ["q0"]
    def epsilonFunction(qi):
        return qi
    return NFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q0",
        epsilonFunction
    )

#** dfa accepts odd string length
def NFA_Odd_Length():
    def transitionFunction(qi, c):
        if qi == "q0":
            return ["q1"]
        else:
            return ["q0"]
    def epsilonFunction(qi):
        return qi
    return NFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1",
        epsilonFunction
    )
#NFA N1 from book page #48
def NFA_N1():
    def transitionFunction(qi, c):
        if qi == "q0" and c == "0":
            return ["q0"]
        elif qi == "q0" and c == "1":
            return ["q0", "q1"]
        elif qi == "q1" and c == "0":
            return ["q2"]
        elif qi == "q2" and c == "1":
            return ["q3"]
        elif qi == "q3" and (c == "0" or c == "1"):
            return ["q3"]
    def epsilonFunction(qi):
        if qi == "q1":
            return ["q2"]

    return NFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2" or qi == "q3",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q3",
        epsilonFunction
    )

#NFA N2 frome book page #51
def NFA_N2():
    def transitionFunction(qi, c):
        if qi == "q0" and c == "0":
            return ["q0"]
        elif qi == "q0" and c == "1":
            return ["q0", "q1"]
        elif qi == "q1" and (c == "0" or c == "1"):
            return ["q2"]
        elif qi == "q2" and (c == "0" or c == "1"):
            return ["q3"]
    def epsilonFunction(qi):
        return []
    return NFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2" or qi == "q3",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q3",
        epsilonFunction
    )

#NFA N4 frome book page #51
def NFA_N4():
    def transitionFunction(qi, c):
        if c == None:
            return self.currentState
        if qi == "q0" and c == "b":
            return ["q1"]
        elif qi == "q0":
            return ["q2"]
        elif qi == "q1" and c == "a":
            return ["q1", "q2"]
        elif qi == "q1" and c == "b":
            return ["q2"]
        elif qi == "q2" and c == "a":
            return ["q0"]
    def epsilonFunction(qi):
        if qi == "q0":
            return ["q2"]
    return NFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        ["a", "b"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q0",
        epsilonFunction
    )


#NFA Three from end is one
def NFA_ThreeFromEndIsOne():
    def transitionFunction(qi, c):
        if qi == "0" and c == "0":
            return ["0"]
        elif qi == "0" and c == "1":
            return ["0", "1"]
        elif qi == "1":
            return ["2"]
        elif qi == "2":
            return ["3"]
        #* qi == 3 *
        else:
            return []
    def epsilonFunction(qi):
        return []
    return NFA(
        lambda qi: qi == "0" or qi == "1" or qi == "2" or qi == "3",
        ["0", "1", "2", "3"],
        "0",
        transitionFunction,
        lambda qi: qi == "3",
        epsilonFunction
    )

#NFA has epsilon
def NFA_HasEps():
    def transitionFunction(qi, c):
        if qi == "0" and c == "0":
            return ["0"]
        elif qi == "1" and c == "0":
            return ["0"]
        elif qi == "1" and c == "1":
            return ["2"]
        elif qi == "2" and c == "0":
            return ["1"]
        elif qi == "2" and c == "1":
            return ["2"]
        else:
            return []
    def epsilonFunction(qi):
        if qi == "0":
            return ["1", "2"]
        else:
            return []

    return NFA(
        lambda qi: qi == "0" or qi == "1" or qi == "2",
        ["0, 1"],
        "0",
        transitionFunction,
        lambda qi: qi == "1",
        epsilonFunction
    )
