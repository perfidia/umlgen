#!/usr/bin/env python

ENTITY_TYPE_SYSTEM = 0
ENTITY_TYPE_HUMAN = 1

class Entity(object):
    def __init__(self, e_id, e_label, e_type):
        self._id = e_id
        self._label = e_label
        self._type = e_type
        self._children = []
        
    def accept(self, v):
        for child in self._children:
            "prevent infinite loops"
            if not v.visited(child):
                child.accept(v)
                
    def add_child(self, child):
        self._children.append(child)

class Process(Entity):
    def __init__(self, p_id, p_label):
        super(Process, self).__init__(p_id, p_label, ENTITY_TYPE_SYSTEM)

class ContextDiagram(object):
    "main object on which the visitor will work"
    def __init__(self, process):
        self._process = process
        
    def accept(self, v):
        self._process.accept(v)
        v.visit_context_diagram(self)
