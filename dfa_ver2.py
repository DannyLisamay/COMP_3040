################################################################################
# DFA VERSION 2 with membership functions
# Used lectures for examples/ideas.
class DFA:
    def __init__(self, statesFunction, alphabet, startState, transitionFunction, acceptFunction):
        self.statesFunction = statesFunction
        self.alpha = alphabet
        self.startState = startState
        self.transitionFunction = transitionFunction
        self.acceptFunction = acceptFunction

    # dfa takes takes string and determines if accepted
    def isStringAccepted(self, s):
        currentState = self.startState
        for x in s:
            currentState = self.transitionFunction(currentState, x)
        return self.acceptFunction(currentState)

    #*******TASK #11************
    #added trace list to DFA and appends states with, pretty similar to task 10
    # transtions through string and appends state to traceList.
    def trace(self, s):
        traceList = []
        currentState = self.startState
        traceList.append(currentState)
        for x in s:
            if currentState != None:
                currentState = self.transitionFunction(currentState, x)
            traceList.append(currentState)
        return traceList

#DFA
#** dfa accepts no strings
# Doesn't accept anything always return false.
def DFA_NoStrings():
    return DFA(
        lambda x: x == 0,
        ["0", "1"],
        0,
        lambda qi, c: 0,
        lambda qi: False,
    )

#** dfa accepts empty string
def DFA_EmptyStrings():
    def transitionFunction(qi, c):
        if (qi == "q0" or qi == "q1") and c == " ":
            return "q1"
        else:
            return "q2"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        [" "],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )

#** dfa function takes charater
#** returns dfa that only accepts strings of that character
def DFA_StringOfChar(char):
    def transitionFunction(qi, c):
        if (qi == "q0" or qi == "q1") and c == char:
            return "q1"
        else:
            return "q2"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        [char],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )

#** dfa accepts even string length
def DFA_Even():
    def transitionFunction(qi, c):
        if qi == "q0":
            return "q1"
        else:
            return "q0"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q0"
    )

#** dfa accepts odd string length
def DFA_Odd():
    def transitionFunction(qi, c):
        if qi == "q0":
            return "q1"
        else:
            return "q0"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )

#** dfa in textbook example figure 1.4 state diagram if M1
def DFA_M1():
    def transitionFunction(qi, c):
        if c == "1":
            return "q1"
        elif qi == "q0":
            return "q0"
        else:
            return "q2"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )

# dfa textbook example figure 1.7 state diagram if M2
def DFA_M2():
    def transitionFunction(qi, c):
        if c == "1":
            return "q1"
        else:
            return "q0"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q1"
    )

# dfa textbook example figure 1.9 state diagram if M3
def DFA_M3():
    def transitionFunction(qi, c):
        if c == "1":
            return "q1"
        else:
            return "q0"

    return DFA(
        lambda qi: qi == "q0" or qi == "q1",
        ["0", "1"],
        "q0",
        transitionFunction,
        lambda qi: qi == "q0"
    )

# dfa textbook example figure 1.12 state diagram if M4
def DFA_M4():
    def transitionFunction(qi, c):
        if c == "a":
            if qi != "r1" and qi != "r2":
                return "q1"
            else:
                return "r2"

        if c == "b":
            if qi != "q1" and qi != "q2":
                return "r1"
            else:
                return "q2"

    return DFA(
        lambda qi: qi == "s" or qi == "q0" or qi == "q1" or qi == "r1" or qi == "r2",
        ["a", "b"],
        "s",
        transitionFunction,
        lambda qi: qi == "q1" or qi == "r1"
    )

#dfa textbook example figure 1.22 Accepts strings contaiing 001
def DFA_Strings001():
    def transitionFunction(qi, c):
        if qi == "q":
            if c == "0":
                return "q0"
            else:
                return "q"
        elif qi == "q0":
            if  c == "0":
                return "q00"
            else:
                return "q"
        elif qi == "q00":
            if c == "0":
                return "q00"
            else:
                return "q001"
        elif qi == "q001":
            return "q001"

    return DFA(
        lambda qi: qi == "q" or qi == "q0" or qi == "q00" or qi == "q001",
        ["0", "1"],
        "q",
        transitionFunction,
        lambda qi: qi == "q001"
    )
