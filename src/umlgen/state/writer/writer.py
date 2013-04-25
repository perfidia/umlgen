import StringIO
from types import MethodType
from lxml import etree as ET
import umlgen.state.model as orginal

def StateDiagram_att_to_xml(self):
	node = ET.Element("state-diagram")
	
	states = ET.SubElement(node, "states")
	for c in self.states:
		c.to_xml(states)

	transitions = ET.SubElement(node, "transitions")
	for c in self.transitions:
		c.to_xml(transitions)
		
	tree = ET.ElementTree(node)
	output = StringIO.StringIO()
	tree.write(output, pretty_print=True, encoding="UTF-8")

	retval = output.getvalue()

	return retval

def State_att_to_xml(self, parent):
	node = ET.SubElement(parent, "state")
	name = ET.SubElement(node, "name")
	name.text = self.name
	on_entry = ET.SubElement(node, "on_entry")
	on_entry.text = self.on_entry
	on_exit = ET.SubElement(node, "on_exit")
	on_exit.text = self.on_exit
	
	return node

def InitialState_att_to_xml(self, parent):
	node = ET.SubElement(parent, "initial-state")
	name = ET.SubElement(node, "name")
	name.text = self.name

	return node

def FinalState_att_to_xml(self, parent):
	node = ET.SubElement(parent, "final-state")
	name = ET.SubElement(node, "name")
	name.text = self.name

	return node

def Transition_att_to_xml(self, parent):
	node = ET.SubElement(parent, "transition")

	predecessor = ET.SubElement(node, "predecessor")
	self.predecessor.to_xml(predecessor)
	successor = ET.SubElement(node, "successor")
	self.successor.to_xml(successor)
	event = ET.SubElement(node, "event")
	event.text = self.event
	precondition = ET.SubElement(node, "precondition")
	precondition.text = self.precondition
	postcondition = ET.SubElement(node, "postcondition")
	postcondition.text = self.postcondition
		
	return node

attachments = {
	orginal.StateDiagram: 		StateDiagram_att_to_xml,
	orginal.State: 			State_att_to_xml,
	orginal.InitialState: 		InitialState_att_to_xml,
	orginal.FinalState: 		FinalState_att_to_xml,
	orginal.Transition: 		Transition_att_to_xml,
}

def attach():
	for clazz in attachments:
		method = attachments[clazz]
		clazz.to_xml = MethodType(method, None, clazz)

def detach():
	for clazz in attachments:
		del clazz.to_xml