from lxml import etree
from StringIO import StringIO
from umlgen.state import model

class XMLReader(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.retval = None;

	def __parseTransition(self, node):
		if node.tag == 'transition':
			for n in node.getchildren():
				if n.tag == 'predecessor':
					for k in n.getchildren():
						for l in k.getchildren():
							if l.tag == 'name':
								for m in self.retval.states:
									if l.text == m.name:
										predecessor = m
				else: 
					if n.tag == 'successor':
						for k in n.getchildren():
							for l in k.getchildren():
								if l.tag == 'name':
									for m in self.retval.states:
										if l.text == m.name:
											successor = m
					else: 
						if n.tag == 'event':
							event = n.text
						else: 
							if n.tag == 'precondition':
								precondition = n.text
							else: 
								if n.tag == 'postcondition':
									postcondition = n.text
								else:
									raise ValueError('Unknown node in transition tag found')
			transition = model.Transition(predecessor, successor, event, precondition, postcondition)
			self.retval.append_transition(transition)
		else:
			raise ValueError('Unknown node in transitions tag found')

	def __parseState(self, node):
		if node.tag == 'state':
			for n in node.getchildren():
				if n.tag == 'name':
					name = n.text
				else: 
					if n.tag == 'on_entry':
						on_entry = n.text
					else: 
						if n.tag == 'on_exit':
							on_exit = n.text
						else:
							raise ValueError('Unknown node in state tag found')
			state = model.State(name, on_entry, on_exit)
			self.retval.append_state(state)
		else: 
			if node.tag == 'initial-state':
				for n in node.getchildren():
					if n.tag == 'name':
						name = n.text
					else:
						raise ValueError('Unknown node in initial-state tag found')
				initial_state = model.InitialState()
				self.retval.append_state(initial_state)
			else: 
				if node.tag == 'final-state':
					for n in node.getchildren():
						if n.tag == 'name':
							name = n.text
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