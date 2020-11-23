import dfa_ver2

# TASK 23
# Define a data type to represent NFAs.
# epsilon is "None"

# Task 24
# Write a (trivial) function that converts DFAs into NFAs.
# Pretty much what was gone over in class.
# My delta is represented with a list, casted to tuple to work with my getAcceptedString function.

def dfa2Nfa(dfa):
    def transitionFunction(qi, c):
        if c == None:
            return tuple([])
        else:
            return tuple([dfa.transitionFunction])
    return DFA(dfa.statesFunction, dfa.alpha, dfa.startState, transitionFunction, dfa.acceptFunction)

# Task 25
# Write a example NFAs.
# casted to tuple to work with my getAcceptedString function. (was an issue with DFAs)

# NFA NoStrings
# Doesn't accept anything always return false.
def NFA_NoStrings():
    return DFA(
        lambda x: x == "0",
        ["0", "1"],
        "0",
        lambda qi, c: "0" or None,
        lambda qi: False,
    )
#** dfa accepts even string length
def NFA_Even_Length():
    def transitionFunction(qi, c):
        # If epsilon return currentState
        if c == None:
            return self.startState

        if qi == "q0":
            return tuple(["q1"])
        else:
            return tuple(["q0"])

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == ["q0"]
    )

#** dfa accepts odd string length
def NFA_Odd_Length():
    def transitionFunction(qi, c):
        # If epsilon return currentState
        if c == None:
            return self.startState

        if qi == "q0":
            return tuple(["q1"])
        else:
            return tuple(["q0"])

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )
#NFA N1 from book page #48
def NFA_N1():
    def transitionFunction(qi, c):
        if qi == "q0" and c == "0":
            return tuple(["q0"])
        elif qi == "q0" and c == "1":
            return tuple(["q0", "q1"])
        elif qi == "q1" and (c == "0" or c == None):
            return tuple(["q2"])
        elif qi == "q2" and c == "1":
            return tuple(["q3"])
        elif qi == "q3" and (c == "0" or c == "1"):
            return tuple(["q3"])

    return dfa_ver2.DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2" or qi == "q3",
        ["0", "1"],
        tuple(["q0"]),
        transitionFunction,
        lambda qi: qi == "q3"
    )

#NFA N2 frome book page #51
def NFA_N2():
    def transitionFunction(qi, c):
        if qi == "q0" and c == "0":
            return tuple(["q0"])
        elif qi == "q0" and c == "1":
            return tuple(["q0", "q1"])
        elif qi == "q1" and (c == "0" or c == "1"):
            return tuple(["q2"])
        elif qi == "q2" and (c == "0" or c == "1"):
            return tuple(["q3"])

    return dfa_ver2.DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2" or qi == "q3",
        ["0", "1"],
        tuple(["q0"]),
        transitionFunction,
        lambda qi: qi == "q3"
    )

#NFA N4 frome book page #51
def NFA_N4():
    def transitionFunction(qi, c):
        if qi == "q0" and c == "b":
            return tuple(["q1"])
        elif qi == "q0" and c == None:
            return tuple(["q2"])
        elif qi == "q1" and c == "a":
            return tuple(["q1", "q2"])
        elif qi == "q1" and c == "b":
            return tuple(["q2"])
        elif qi == "q2" and c == "a":
            return tuple(["q0"])

    return dfa_ver2.DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        ["a", "b"],
        tuple(["q0"]),
        transitionFunction,
        lambda qi: qi == "q0"
    )


#NFA Three from end is one
def NFA_ThreeFromEndIsOne():
    def transitionFunction(qi, c):
        # If epsilon return currentState
        if c == None:
            return tuple([self.startState])
        else:
            if qi == "0" and c == "0":
                return tuple(["0"])
            elif qi == "0" and c == "1":
                return tuple(["0", "1"])
            elif qi == "1":
                return tuple(["2"])
            elif qi == "2":
                return tuple(["3"])
            # return currentState
            elif qi == "3":
                return tuple([self.startState])
    return dfa_ver2.DFA(
        lambda qi: qi == "0" or qi == "1" or qi == "2" or qi == "3",
        ["0", "1", "2", "3"],
        "0",
        transitionFunction,
        lambda qi: qi == "3"
    )
