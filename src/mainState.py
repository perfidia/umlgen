#!/usr/bin/env python

from umlgen.state.model import *
from umlgen.state.writer import XMLWriter

def main():
	initial = InitialState()
	s1 = State("Opened")
	initial.appendSuccessor(s1)
	s1.appendPredecessor(initial)
	transition_initial_s1 = Transition(initial, s1, "Create")
	final = FinalState()
	s1.appendSuccessor(final)
	final.appendPredecessor(s1)
	transition_s1_final = Transition(s1, final, "Destroy")
	myStateDiagram = StateDiagram()
	myStateDiagram.appendState(initial)
	myStateDiagram.appendState(s1)
	myStateDiagram.appendState(final)
	myStateDiagram.appendTransition(transition_initial_s1)
	myStateDiagram.appendTransition(transition_s1_final)
	
	f = open("test.xml",'w');
	XMLWriter(myStateDiagram).execute(f)
	f.close();
	
	return

if __name__ == "__main__":
    main()
    