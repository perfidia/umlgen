import StringIO
from types import MethodType
from lxml import etree as ET
import umlgen.state.model as orginal

def StateDiagram_att_to_xml(self):
	node = ET.Element("state-diagram")

	for c in self.states:
		c.to_xml(node)

	for c in self.transitions:
		c.to_xml(node)
		
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
	on_exit.text = self.name

	predecessors = ET.SubElement(node, "predecessors")

	for c in self.predecessors:
		c.to_xml(predecessors)

	successors = ET.SubElement(node, "successors")

	for c in self.successors:
		c.to_xml(successors)
		
	return node

def InitialState_att_to_xml(self, parent):
	node = ET.SubElement(parent, "initial-state")

	successors = ET.SubElement(node, "successors")

	for c in self.successors:
		c.to_xml(successors)

	return node

def FinalState_att_to_xml(self, parent):
	node = ET.SubElement(parent, "final-state")

	predecessors = ET.SubElement(node, "predecessors")

	for c in self.predecessors:
		c.to_xml(predecessors)

	return node

def Transition_att_to_xml(self, parent):
	node = ET.SubElement(parent, "transition")

	predecessor = ET.SubElement(node, "predecessor")
	predecessor.text = self.predecessor
	successor = ET.SubElement(node, "successor")
	successor.text = self.successor
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