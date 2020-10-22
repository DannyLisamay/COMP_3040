#Danny Lisamay
#9/15
#*******TASK #4
#Created DFA class
class DFA:
    def __init__(self, states, alphabet, transitionFunction, startState, acceptStates):
        self.states = states
        self.alpha = alphabet
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
    # old way used a map / new one takes function
    # transition to next state given key [state, char]
    # checks if key is in transitionFunction if so transition if not return null
    #def transitionToState(self, c):
    #    if ((self.currentState, c) in self.transitionFunction.keys()):
    #        self.currentState = self.transitionFunction[(self.currentState, c)]
    #        return
    #    self.currentState = None
    #    return

    #def transitionToState(self, c):
    #    if ((self.currentState, c) in self.transitionFunction.keys()):
    #        self.currentState = self.transitionFunction[(self.currentState, c)]
    #        return
    #    self.currentState = None
    #    return

    #*******TASK #10************
    # dfa takes takes string and determines if accepted
    def isStringAccepted(self, s):
        self.currentState = self.startState
        for x in s:
            #mapping
            #self.transitionToState(x)
            #function
            if self.currentState != None:
                self.currentState = self.transitionFunction(self, x)
        return self.inAcceptState()

    #*******TASK #11************
    #added trace list to DFA and appends states with, pretty similar to task 10
    # transtions through string and appends state to traceList.
    def trace(self, s):
        traceList = []
        self.currentState = self.startState
        traceList.append(self.currentState)
        for x in s:
            #mapping
            #self.transitionToState(x)
            #function
            if self.currentState != None:
                self.currentState = self.transitionFunction(self, x)
            traceList.append(self.currentState)
        return traceList

    #*******TASK #11************
    # Maybe like DFS search?
    def getAcceptedString(self):
        # Checks if accepted states are in states list
        if not set(self.acceptStates).intersection(self.states):
            return False
        return self.DFS()
    # helper function for task 11
    # DFS kinda?
    def DFS(self):
        # accept strings
        acceptedString = []
        # list all states set to False
        visited = [False] * len(self.states)
        visited[self.states.index(self.currentState)]
        # stack used for dfs
        stack = []
        # appends first state to stack
        stack.append(self.currentState)
        # checks if init state is accepted string will be empty
        if self.currentState in self.acceptStates:
            return acceptedString
        # checks for accepted
        for x in self.alpha:
            # takes alphabet char and visted list:
            #check if next state in transition has been visited
            while not visited[self.states.index(self.transitionFunction(self, x))]:
                acceptedString.append(x)
                visited[self.states.index(self.currentState)] = True
                self.currentState = self.transitionFunction(self, x)
                if self.inAcceptState():
                    return acceptedString

#DFAs
#*******TASK #5************
#** dfa accepts no strings
def DFA_NoStrings():
    states = ["q0"]
    # always return q0 and no accept state
    # transitionFunction = dict()
    #transitionFunction[("q0", "")] = "q0"
    #transitionFunction[("q0", "0")] = "q0"
    def transitionFunction(self, c):
        return states[0]
    return DFA(states, ["0"], transitionFunction , states[0], [])

#********TASK #6************
#** dfa accepts empty string
# empty and non empty sting used for Testing
def DFA_EmptyStrings():
    states = ["q0", "q1"]
    #transitionFunction = dict()
    #transitionFunction[("q0", "")] = "q1"
    #transitionFunction[("q1", "")] = "q1"
    def transitionFunction(self, c):
        if c == " " :
            return states[1]
        else:
            return None
    return DFA(states, [" ","0","1"], transitionFunction, states[0], ["q1"])

#********TASK #7************
#*** dfa function takes charater and returns dfa that only accepts strings of that character
# once a charater is not c dfa state goes to null
def DFA_StringOfChar(char):
    states = ["q0", "q1"]
    #transitionFunction = dict()
    #transitionFunction[("q0", c)] = "q1"
    #transitionFunction[("q1", c)] = "q1"
    def transitionFunction(self, c):
        if c == char:
            return states[1]
        else:
            return None
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

#********TASK #8************
#DFA examples
# dfa accepts even string length
def DFA_Even():
    states = ["qEven", "qOdd"]
    #transitionFunction = dict()
    #transitionFunction[("qEven", "0")] = "qOdd"
    #transitionFunction[("qEven", "1")] = "qOdd"
    #transitionFunction[("qOdd", "0")] = "qEven"
    #transitionFunction[("qOdd", "1")] = "qEven"
    def transitionFunction(self, c):
        if self.currentState == states[0]:
            return states[1]
        else:
            return states[0]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["qEven"])

# dfa accepts odd string length
def DFA_Odd():
    states = ["qEven", "qOdd"]
    #transitionFunction = dict()
    #transitionFunction[("qEven", "0")] = "qOdd"
    #transitionFunction[("qEven", "1")] = "qOdd"
    #transitionFunction[("qOdd", "0")] = "qEven"
    #transitionFunction[("qOdd", "1")] = "qEven"
    def transitionFunction(self, c):
        if self.currentState == states[0]:
            return states[1]
        else:
            return states[0]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["qOdd"])

# dfa in textbook example figure 1.4 state diagram if M1
def DFA_M1():
    states = ["q0", "q1", "q2"]
    #transitionFunction = dict()
    #transitionFunction[("q0", "0")] = "q0"
    #transitionFunction[("q0", "1")] = "q1"
    #transitionFunction[("q1", "0")] = "q2"
    #transitionFunction[("q1", "1")] = "q1"
    #transitionFunction[("q2", "0")] = "q1"
    #transitionFunction[("q2", "1")] = "q1"
    def transitionFunction(self, c):
        if c == "1":
            return states[1]
        elif self.currentState == states[0]:
            return states[0]
        else:
            return states[2]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

# dfa textbook example figure 1.7 state diagram if M2
def DFA_M2():
    states = ["q0","q1"]
    #transitionFunction = dict()
    #transitionFunction[("q0","0")] = "q0"
    #transitionFunction[("q0","1")] = "q1"
    #transitionFunction[("q1","0")] = "q0"
    #transitionFunction[("q1","1")] = "q1"
    def transitionFunction(self, c):
        if c == "1":
            return states[1]
        else:
            return states[0]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q1"])

# dfa textbook example figure 1.9 state diagram if M3
def DFA_M3():
    states = ["q0","q1"]
    #transitionFunction = dict()
    #transitionFunction[("q0","0")] = "q0"
    #transitionFunction[("q0","1")] = "q1"
    #transitionFunction[("q1","0")] = "q0"
    #transitionFunction[("q1","1")] = "q1"
    def transitionFunction(self, c):
        if c == "1":
            return states[1]
        else:
            return states[0]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q0"])

# dfa textbook example figure 1.12 state diagram if M4
def DFA_M4():
    states = ["s", "q1", "q2", "r1", "r2"]
    #transitionFunction = dict()
    #transitionFunction[("s","a")] = "q1"
    #transitionFunction[("s","b")] = "r1"
    #transitionFunction[("q1","a")] = "q1"
    #transitionFunction[("q1","b")] = "q2"
    #transitionFunction[("q2","a")] = "q1"
    #transitionFunction[("q2","b")] = "q2"
    #transitionFunction[("r1","a")] = "r2"
    #transitionFunction[("r1","b")] = "r1"
    #transitionFunction[("r2","a")] = "r2"
    #transitionFunction[("r2","b")] = "r1"
    def transitionFunction(self, c):
        if c == "a":
            if self.currentState != states[3] and self.currentState != states[4]:
                return states[1]
            else:
                return states[4]

        if c == "b":
            if self.currentState != states[1] and self.currentState != states[2]:
                return states[3]
            else:
                return states[2]

    return DFA(states, ["a","b"], transitionFunction, states[0], ["q1","r1"])

#dfa textbook example figure 1.22 Accepts strings contaiing 001
def DFA_Strings001():
    states = ["q", "q0", "q00", "q001"]
    #transitionFunction = dict()
    #transitionFunction[("q","0")] = "q0"
    #transitionFunction[("q","1")] = "q"
    #transitionFunction[("q0","0")] = "q00"
    #transitionFunction[("q0","1")] = "q"
    #transitionFunction[("q00","0")] = "q00"
    #transitionFunction[("q00","1")] = "q001"
    #transitionFunction[("q001","0")] = "q001"
    #transitionFunction[("q001","1")] = "q001"
    def transitionFunction(self, c):
        if self.currentState == states[0]:
            if c == "0":
                return states[1]
            else:
                return states[0]
        elif self.currentState == states[1]:
            if  c == "0":
                return states[2]
            else:
                return states[0]
        elif self.currentState == states[2]:
            if c == "0":
                return states[2]
            else:
                return states[3]
        else:
            return states[3]
    return DFA(states, ["0","1"], transitionFunction, states[0], ["q001"])
