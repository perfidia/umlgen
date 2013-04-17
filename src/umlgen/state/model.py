class StateDiagram(object):
	def __init__(self):
		self.states = []
		self.transitions = []

	def appendState(self, state):
		self.states.append(state)
		
		return self
		
	def appendTransition(self, transition):
		self.transitions.append(transition)

		return self
		
class State(object):
	def __init__(self, name, on_entry = None, on_exit = None, predecessors = None, successors = None):
		self.name = name
		self.on_entry = on_entry
		self.on_exit = on_exit
		self.predecessors = []
		self.successors = []

		if predecessors:
			for predecessor in predecessors:
				self.appendPredecessor(predecessor)
				
		if successors:
			for successor in successors:
				self.appendSuccessor(successor)

	def appendPredecessor(self, predecessor):
		self.predecessors.append(predecessor)
		
		return self
		
	def appendSuccessor(self, successor):
		self.successors.append(successor)

		return self
		
class InitialState(State):
	def __init__(self, successors = None):
		State.__init__(self, "initial")
		
class FinalState(State):
	def __init__(self, predecessors = None):
		State.__init__(self, "final")

class Transition(object):
	def __init__(self, predecessor, successor, event, precondition = None, postcondition = None):
		self.predecessor = predecessor
		self.successor = successor
		self.event = event
		self.precondition = precondition
		self.postcondition = postcondition