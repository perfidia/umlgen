from lxml import etree
from StringIO import StringIO
from umlgen.state import model

class XMLReader(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.retval = None;

	def __parseTransition(self, node):
		for n in node.getchildren():
			if n.tag == 'transition':
				for f in n.getchildren():
					if f.tag == 'predecessor':
						predecessor = f.text
					else: 
						if f.tag == 'successor':
							successor = f.text
						else: 
							if f.tag == 'event':
								event = f.text
							else: 
								if f.tag == 'precondition':
									precondition = f.text
								else: 
									if f.tag == 'postcondition':
										postcondition = f.text
									else:
										raise ValueError('Unknown node in transition tag found')
				transition = model.Transition(predecessor, successor, event, precondition, postcondition)
				self.retval.append_transition(transition)
			else:
				raise ValueError('Unknown node in transitions tag found')

	def __parseState(self, node):
		for n in node.getchildren():
			if n.tag == 'state':
				for f in n.getchildren():
					if f.tag == 'name':
						name = f.text
					else: 
						if f.tag == 'on_entry':
							on_entry = f.text
						else: 
							if f.tag == 'on_exit':
								on_exit = f.text
							else:
								raise ValueError('Unknown node in state tag found')
				state = model.State(name, on_entry, on_exit)
				self.retval.append_state(state)
			else: 
				if n.tag == 'initial-state':
					for f in n.getchildren():
						if f.tag == 'name':
							name = f.text
						else:
							raise ValueError('Unknown node in initial-state tag found')
					initial_state = model.InitialState()
					self.retval.append_state(initial_state)
				else: 
					if n.tag == 'final-state':
						for f in n.getchildren():
							if f.tag == 'name':
								name = f.text
							else:
								raise ValueError('Unknown node in final-state tag found')
						final_state = model.FinalState()
						self.retval.append_state(final_state)
					else:
						raise ValueError('Unknown node in states tag found')

	def __parseStateDiagram(self, node):
		if node.tag != 'state-diagram':
			raise ValueError('Tag state-diagram not found')

		self.retval = model.StateDiagram()

		for n in node.getchildren():
			if n.tag == 'states':
				for s in n.getchildren():
					self.__parseState(s)
			else:
				if n.tag == 'transitions':
					for t in n.getchildren():
						self.__parseTransition(t)
				else:
					raise ValueError('Unknown node in state-diagram tag found')

	def execute(self):
		root = etree.fromstring(self.input_data)

		self.__parseStateDiagram(root)

		return self.retval