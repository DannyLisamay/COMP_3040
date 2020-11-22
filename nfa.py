# TASK 23
# Define a data type to represent NFAs.
# epsilon is "None"
class NFA:
    def __init__(self, statesFunction, alphabet, startState, transitionFunction, acceptFunction):
        self.statesFunction = statesFunction
        self.alpha = alphabet
        self.startState = startState
        self.transitionFunction = transitionFunction
        self.acceptFunction = acceptFunction

# Task 24
# Write a (trivial) function that converts DFAs into NFAs.
# Pretty much what was gone over in class.
# My delta is represented with a list, casted to tuple to work with my getAcceptedString function.

def dfa2Nfa(dfa):
    transitionFunction = tuple([dfa.transitionFunction])
    return return NFA(dfa.statesFunction, dfa.alpha, dfa.startState, transitionFunction, dfa.acceptFunction)


# Task 25
# Write a example NFAs.
# casted to tuple to work with my getAcceptedString function. (was an issue with DFAs)
def NFA_ThreeFromEndIsOne():
    def transitionFunction(qi, c):
        if qi == "0" and c == "0":
            return "0"
        else if qi == "0" and c == "1":
            return tuple([0, 1])

    return DFA(
        lambda qi: qi == "0" or qi == "1" or qi == "2" or qi == "3",
        ["0", "1", "2", "3"],
        "0",
        transitionFunction,
        lambda qi: qi == "3"
    )
