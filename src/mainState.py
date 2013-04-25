#!/usr/bin/env python

from umlgen.state.model import *
from umlgen.state.writer import XMLWriter
from umlgen.state.reader import XMLReader

def main():
	initial = InitialState()
	s1 = State("Opened")
	transition_initial_s1 = Transition(initial, s1, "Create")
	final = FinalState()
	transition_s1_final = Transition(s1, final, "Destroy")
	myStateDiagram = StateDiagram()
	myStateDiagram.append_state(initial)
	myStateDiagram.append_state(s1)
	myStateDiagram.append_state(final)
	myStateDiagram.append_transition(transition_initial_s1)
	myStateDiagram.append_transition(transition_s1_final)
	
	f = open("test.xml",'w');
	XMLWriter(myStateDiagram).execute(f)
	f.close();
	
	input_data = open("test.xml").read()
	retval = XMLReader(input_data).execute()
	f = open("reverseTest.xml",'w');
	XMLWriter(retval).execute(f)
	f.close();
	return

if __name__ == "__main__":
    main()
    