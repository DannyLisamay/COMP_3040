#Danny Lisamay
#9/15
#Created DFA class
#9/16
#Started Task 6
class dfa:
    def __init__(self, states, alphabet, transitionFunction, startState, acceptStates):
        self.states = states
        self.aplha = alphabet
        self.transition = transitionFunction
        self.currentState = startState
        self.acceptStates = acceptStates

    def setState(self, s):
        self.currentState = s

    def isValid(self):
        valid = False
        for x in range(len(self.acceptStates)):
            if x == self.currentState:
                valid = True
        return valid
