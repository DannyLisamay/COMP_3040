#Danny Lisamay
#9/15
#*******TASK #4
#Created DFA class
# state list
# alphabet
# list of transition pairs
# start state
# list of accept
class State:
    #transition is a list that contains pairs
    transitions = []
    def __init__(self, name, acceptStatus):
        self.name = name
        self.acceptStatus = acceptStatus
    #get name
    def getName(self):
        return self.name
    #get acceptStatus
    def getAcceptStatus(self):
        return self.acceptStatus
    #insert Transition
    def insertTransition(self, name, transitionValue):
        self.transition.insert([name,transitionValue])

class DFA:
    def __init__(self, states, alphabet, transitionFunction, startState, acceptStates):
        self.states = states
        self.aplha = alphabet
        self.transition = transitionFunction
        self.currentState = startState
        self.acceptStates = acceptStates
    #set State
    def setState(self, s):
        self.currentState = s
    #get currentState
    def getCurrentState(self):
        return self.currentState
