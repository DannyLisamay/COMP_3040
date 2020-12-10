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
            traceList.append(list(currentState))
        return traceList

    #*******TASK #12************
    # Given a DFA and a string, returns the trace of configurations it visits.
    # Like a BFS?
    def getAcceptedString(self):
        currentState =self.startState
        # String list
        string = []
        # Visted list dictionary
        visted = { tuple(currentState) : True}
        # States that are going to be visted.
        queue = [currentState]
        # While queue not empty
        while queue:
            # current state is set to whate in the queue
            currentState = queue.pop(0)
            # checks if were in accepted state return string
            if self.acceptFunction(currentState):
                return string
            # for each charater in the alphabet
            for c in self.alpha:
                # next state set to next state in transition according to givin charater
                nextState = self.transitionFunction(currentState, c)
                # if next state has yet to be visited
                if not visted.get(tuple(nextState)):
                    # in visted dictionary set to True
                    visted[tuple(nextState)] = True
                    # add next state to queue
                    queue.append(nextState)
                    # add charater to string
                    string.append(c)
        # Didn't find accepted state
        return False

    #*******TASK #13************
    # Takes one DFA and returns a DFA that accepts that the given one does not (and vice versa).
    # uses lambda to return complment of acceptFunction
    # I should have created this outside of DFA class. But it works this way.
    def complement(self):
        return DFA(self.statesFunction, self.alpha, self.startState, self.transitionFunction, lambda qi: not self.acceptFunction(qi))

#*******TASK #14************
# Takes two DFAs and returns a third DFA that accepts a string if either argument accepts it.
def union(Qa, Qb):
    # Elemnets of Qa paired with Elements of Qb
    statesFunction = lambda qi: Qa.statesFunction(qi[0]) or Qb.statesFunction(qi[1])
    # alphabet pair Qa, Qb
    alpha = tuple([Qa.alpha, Qb.alpha])
    # start state pair Qa, Qb
    startState = tuple([Qa.startState, Qb.startState])
    # transition return pair Qa.transitionFunction(qi[0]) and Qb.transitionFunction(qi[1]
    transitionFunction = lambda qi, c: tuple([Qa.transitionFunction(qi[0], c), Qb.transitionFunction(qi[1], c)])
    # acceptFunction returns true if either Qa.acceptFunction(qi[0]) or Qb.acceptFunction(qi[1]) is true
    acceptFunction = lambda qi: Qa.acceptFunction(qi[0]) or Qb.acceptFunction(qi[1])
    return DFA(statesFunction, alpha, startState, transitionFunction, acceptFunction)

#*******TASK #16************
# Takes two DFAs and returns a third DFA that accepts a string if both arguments accepts it.
# Similar to task #14, however for the acceptFunction instead of acceptFunction
# True for Qa or Qb, its acceptFunction True Qa and Qb.
def intersection(Qa, Qb):
    # Elemnets of Qa paired with Elements of Qb
    statesFunction = lambda qi: Qa.statesFunction(qi[0]) and Qb.statesFunction(qi[1])
    # alphabet pair Qa, Qb
    alpha = tuple([Qa.alpha, Qb.alpha])
    # start state pair Qa, Qb
    startState = tuple([Qa.startState, Qb.startState])
    # transition return pair Qa.transitionFunction(qi[0]) and Qb.transitionFunction(qi[1]
    transitionFunction = lambda qi, c: tuple([Qa.transitionFunction(qi[0], c), Qb.transitionFunction(qi[1], c)])
    # acceptFunction returns true for both Qa.acceptFunction(qi[0]) and Qb.acceptFunction(qi[1]) is true
    acceptFunction = lambda qi: Qa.acceptFunction(qi[0]) and Qb.acceptFunction(qi[1])
    return DFA(statesFunction, alpha, startState, transitionFunction, acceptFunction)

#*******TASK #18*************
# Takes two DFAs (X and Y) and returns whether every string accepted by X is also accepted by Y.
# Returns if every string in Qa is also accepted by Qb
# returns True if empty
def subset(Qa, Qb):
    return (intersection(Qb.complement(), Qa)).getAcceptedString() == False

#*******TASK #20*************
#function which takes two DFAs (X and Y) and returns whether every string accepted by X is also accepted by Y and vice versa.
def equality(Qa, Qb):
    return subset(Qa, Qb) and subset(Qb, Qa)

####################################
#DFA
#** dfa accepts no strings
# Doesn't accept anything always return false.
def DFA_NoStrings():
    return DFA(
        lambda x: x == "0",
        ["0", "1"],
        "0",
        lambda qi, c: "0",
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

#** dfa textbook example figure 1.7 state diagram if M2
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

#** dfa textbook example figure 1.9 state diagram if M3
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

#** dfa textbook example figure 1.12 state diagram if M4
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

#** dfa textbook example figure 1.22 Accepts strings contaiing 001
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

#** dfa accepts 0 or 1
def DFA_ZeroOrOnes():
    def transitionFunction(qi, c):
        if qi == ("q0" or qi == "q1") and (c == "0" or c == "1"):
            return "q1"
    return DFA(
        lambda qi: qi == "q0" or qi == "q1" or qi == "q2",
        ["0", "1"],
        "0",
        transitionFunction,
        lambda qi: qi == "1"
    )
