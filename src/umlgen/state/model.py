# -*- coding: utf-8 -*-

class StateDiagram(object):
	def __init__(self):
		self.states = []
		self.transitions = []

	def append_state(self, state):
		self.states.append(state)

		return self

	def append_transition(self, transition):
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
			self.predecessors = predecessors

		if successors:
			self.successors = successors

	def append_predecessor(self, predecessor):
		self.predecessors.append(predecessor)

		return self

	def append_successor(self, successor):
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
