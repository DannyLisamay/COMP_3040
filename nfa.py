import dfa_ver2
from itertools import chain

#*******TASK #23 ************
# Define a data type to represent NFAs.
# Epsilon is treated as a seperate transition function
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
# Epsilon is treated as a seperate transition function
def dfa2Nfa(dfa):
    def transitionFunction(qi, c):
        return [dfa.transitionFunction]
    def epsilonFunction(qi):
        return []
    return NFA(dfa.statesFunction, dfa.alpha, dfa.startState, transitionFunction, dfa.acceptFunction, epsilonFunction)


#*******TASK #27 ************
#Write a function that given an NFA, a string, a trace, and a boolean,
#determines if the trace is a valid execution of the NFA and accepts results in the given boolean.
def oracle(nfa, trace, result):
    return oracle_(nfa, nfa.startState, trace, result)

#Helper function
def oracle_(nfa, qi, trace, result):
    # Check if trace is empty, returns if in acceptFunction
    if not trace:
        return result == nfa.acceptFunction(qi)
    # te is first element tp is rest
    [te, *tp] = trace
    # Tr
    def qjs():
        # check if te is epsilon
        if len(te) == 1:
            # epsilon transition function
            return nfa.epsilonFunction(qi)
        else:
            # transitionFunction
            return nfa.transitionFunction(qi, te[1])
    # Recursivly go through each element in trace.
    return te[0] in qjs() and oracle_(nfa, te[0], tp, result)

#*******TASK #30 ************
# Write a function that given an NFA and a string, returns a tree of all possible traces.
# Not working correctly.
def forking(nfa, s):
    return forking_(nfa, nfa.startState ,s)

#Helper function
def forking_(nfa, qi ,s):
    # continue through string function
    def cont(sp):
        def qj(qj):
            children.append(forking_(nfa, qj, sp))
        return qj(sp)
    children = []
    for q in nfa.epsilonFunction(qi):
        cont(s)
    if not s:
        children.append(nfa.acceptFunction(qi))
    else:
        [s0, *sp] = s
        for q in nfa.transitionFunction(qi, s0):
            cont(sp)
    return [qi, children]

#*******TASK #36 ************
# Write a function that takes an NFA and returns a new NFA that accepts a string
# if it can be broken into N pieces, each accepted by the argument.
def kleeneStar(x):
    statesFunction = lambda qi: qi == 0 or (qi[0] == 'x' and x.statesFunction(qi[1]))
    alpha = self.alpha
    startState = 0
    def transitionFunction(qi ,c):
        if qi == 0:
            return []
        elif qi[0] == 'x':
            tag("x", x.transitionFunction(qi[1], c))
        else:
            return []
    acceptFunction = lambda qi: qi == 0
    def epsilonFunction(qi):
        if qi == 0:
            return [['x', x.startState]]
        elif qi[0] == 'x':
            tag("x", _epsilonFunction(qi))
        else:
            return []
    #epsilonFunction helper
    def _epsilonFunction(qi):
        if x.epsilonFunction(qi[1]).append(x.acceptFunction(qi[1])):
            return [0]
        else:
            return []
    acceptFunction = lambda qi: qi == 0
    return DFA(statesFunction, alpha, startState, transitionFunction, acceptFunction, epsilonFunction)

#Helper function tag
def tag(tag, objs):
    return map(lambda o: [tag, o], objs)

#*******TASK #38 ************
# Write a function which converts an NFA into a DFA that accepts the same language.
def nfa2dfa(nfa):
    #E function follows all episoln transitions
    def E(qd):
        qdp = qd
        addedAny = True
        # Seen list set all to false
        seen = {}
        for qn in qdp:
            seen = {qn : False}
        while(addedAny):
            addedAny = False
            # Itterate over qdp
            for qn in qdp:
                # Itterate over each element return by epsilonFunction
                for qne in nfa.epsilonFunction(qn):
                    if not (seen[qne]):
                        seen[qne] = True
                        qdp.append(qne)
                        addedAny = True
        return qdp
    # statesFunction checks if all elements given array is accepted by nfa statesFunction
    def statesFunction(qd):
        temp = False
        for qde in nfa.statesFunction(qd):
            temp = qde
        return temp
    # startState is the set of nfa startState
    startState = E([ nfa.startState ])
    # transitionFunction
    def transitionFunction(qd, c):
        # Itterate transitionFunction through all element for a flatten list of list.
        return E(map(lambda qn: nfa.transitionFunction(qn, c), (qd)))
    # flatten list of list used for transitionFunction
    def flatten(listOfLists):
        #rint(list(chain.from_iterable(listOfLists)))
        return list(chain.from_iterable(listOfLists))
    # acceptFunction checks if any elements given array is accepted by nfa statesFunction
    def acceptFunction(qd):
        for qde in qd:
            if nfa.acceptFunction(qde) == True:
                return True
        return False
    return dfa_ver2.NFA(statesFunction, nfa.alpha, startState, transitionFunction, acceptFunction)

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
        lambda qi: "q1",
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
        lambda qi: qi == ["q0"],
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
        lambda qi: qi == ["q1"],
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
        else:
            return []
    def epsilonFunction(qi):
        if qi == "q1":
            return ["q2"]
        else:
            return []

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

#NFA one blah blah, inclass example
def NFA_OneBB():
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
        ["0, 1"],
        "0",
        transitionFunction,
        lambda qi: qi == "3",
        epsilonFunction
    )
