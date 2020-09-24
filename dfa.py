#Danny Lisamay
#9/15
#*******TASK #4
#Created DFA class
class DFA:
    trace = []
    def __init__(self, states, alphabet, transitionFunction, startState, acceptStates):
        self.states = states
        self.aplha = alphabet
        self.transitionFunction = transitionFunction
        self.startState = startState
        self.acceptStates = acceptStates

        self.currentState = startState
    #set State
    def setState(self, s):
        self.currentState = s
    #get currentState
    def getCurrentState(self):
        return self.currentState
    # bool if state is in acceptStates list
    def inAcceptState(self):
        return self.currentState in self.acceptStates
    # Helper function for task 10
    # transition to next state given key [state, char]
    # checks if key is in transitionFunction if so transition if not return null
    def transitionToState(self, c):
        if ((self.currentState, c) in self.transitionFunction.keys()):
            self.currentState = self.transitionFunction[(self.currentState, c)]
            return
        self.currentState = None
        return
    #*******TASK #10************
    # dfa takes takes string and determines if accepted
    def isStringAccepted(self, s):
        self.currentState = self.startState
        self.trace.clear()
        for x in s:
            self.transitionToState(x)
            self.trace.append(self.currentState)
        return self.inAcceptState()
    #*******TASK #11************
    #added trace list to DFA and appends states with isStringAccepted method
    def printTrace(self):
        s = self.startState
        for x in self.trace:
            if x != None:
                s += " -> " + x
            else:
                s += " -> " + "None"
        print(s)

#DFAs
#*******TASK #5************
#** dfa accepts no strings
def DFA_NoStrings():
    states = ["q0"]
    #kinda pointless, always return q0 and no accept state
    transitionFunction = dict()
    transitionFunction[("q0", "")] = "q0"
    transitionFunction[("q0", "0")] = "q0"
    return DFA(states, ["0"], transitionFunction , states[0], [])

#********TASK #6************
#** dfa accepts empty string
# empty and non empty sting used for Testing
def DFA_EmptyStrings():
    states = ["q0", "q1"]
    transitionFunction = dict()
    transitionFunction[("q0", "")] = "q1"
    transitionFunction[("q0", "0")] = "q0"
    transitionFunction[("q0", "1")] = "q0"
    transitionFunction[("q1", "")] = "q1"
    transitionFunction[("q1", "0")] = "q0"
    transitionFunction[("q1", "1")] = "q0"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

#********TASK #7************
#*** dfa function takes charater and returns dfa that only accepts strings of that character
# once a charater is not c dfa state goes to null
def DFA_StringOfChar(c):
    states = ["q0", "q1"]
    transitionFunction = dict()
    transitionFunction[("q0", c)] = "q1"
    transitionFunction[("q1", c)] = "q1"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

#********TASK #8************
#DFA examples
# dfa accepts even string length
def DFA_Even():
    states = ["qEven", "qOdd"]
    transitionFunction = dict()
    transitionFunction[("qEven", "0")] = "qOdd"
    transitionFunction[("qEven", "1")] = "qOdd"
    transitionFunction[("qOdd", "0")] = "qEven"
    transitionFunction[("qOdd", "1")] = "qEven"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["qEven"])

# dfa accepts odd string length
def DFA_Odd():
    states = ["qEven", "qOdd"]
    transitionFunction = dict()
    transitionFunction[("qEven", "0")] = "qOdd"
    transitionFunction[("qEven", "1")] = "qOdd"
    transitionFunction[("qOdd", "0")] = "qEven"
    transitionFunction[("qOdd", "1")] = "qEven"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["qOdd"])

# dfa in textbook example figure 1.4 state diagram if M1
def DFA_M1():
    states = ["q0", "q1", "q3"]
    transitionFunction = dict()
    transitionFunction[("q0", "0")] = "q0"
    transitionFunction[("q0", "1")] = "q1"
    transitionFunction[("q1", "0")] = "q2"
    transitionFunction[("q1", "1")] = "q1"
    transitionFunction[("q2", "0")] = "q1"
    transitionFunction[("q2", "1")] = "q1"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

# dfa textbook example figure 1.7 state diagram if M2
def DFA_M2():
    states = ["q0","q1"]
    transitionFunction = dict()
    transitionFunction[("q0","0")] = "q0"
    transitionFunction[("q0","1")] = "q1"
    transitionFunction[("q1","0")] = "q0"
    transitionFunction[("q1","1")] = "q1"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

# dfa textbook example figure 1.9 state diagram if M3
def DFA_M3():
    states = ["q0","q1"]
    transitionFunction = dict()
    transitionFunction[("q0","0")] = "q0"
    transitionFunction[("q0","1")] = "q1"
    transitionFunction[("q1","0")] = "q0"
    transitionFunction[("q1","1")] = "q1"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q0"])

# dfa textbook example figure 1.12 state diagram if M4
def DFA_M4():
    states = ["s", "q1", "q2", "r1", "r2"]
    transitionFunction = dict()
    transitionFunction[("s","a")] = "q1"
    transitionFunction[("s","b")] = "r1"
    transitionFunction[("q1","a")] = "q1"
    transitionFunction[("q1","b")] = "q2"
    transitionFunction[("q2","a")] = "q1"
    transitionFunction[("q2","b")] = "q2"
    transitionFunction[("r1","a")] = "r2"
    transitionFunction[("r1","b")] = "r1"
    transitionFunction[("r2","a")] = "r2"
    transitionFunction[("r2","b")] = "r1"
    return DFA(states, ["a","b"], transitionFunction, states[0], ["q1","r1"])

#dfa textbook example figure 1.22 Accepts strings contaiing 001
def DFA_Strings001():
    states = ["q", "q0", "q00", "q001"]
    transitionFunction = dict()
    transitionFunction[("q","0")] = "q0"
    transitionFunction[("q","1")] = "q"
    transitionFunction[("q0","0")] = "q00"
    transitionFunction[("q0","1")] = "q"
    transitionFunction[("q00","0")] = "q00"
    transitionFunction[("q00","1")] = "q001"
    transitionFunction[("q001","0")] = "q001"
    transitionFunction[("q001","1")] = "q001"
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q001"])
