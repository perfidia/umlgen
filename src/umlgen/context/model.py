#!/usr/bin/env python

ENTITY_TYPE_SYSTEM = 1
ENTITY_TYPE_HUMAN = 2

class Entity(object):
    def __init__(self, e_id, e_label, e_type):
        self._id = e_id
        self._label = e_label
        self._type = e_type
        self._children = []
        
    def get_id(self):
        return self._id
    
    def get_label(self):
        return self._label
    
    def get_type(self):
        return self._type
    
    def get_children(self):
        return self._children;
        
    def _accept_children(self, v):
        for child in self._children:
            #prevent infinite loops
            if not v.visited(child["child"]):
                child["child"].accept(v)
        
    def accept(self, v):
        self._accept_children(v)
        v.visit_entity(self)
                
    def add_child(self, child, connection):
        self._children.append({ "child": child, "connection": connection })


class Process(Entity):
    def __init__(self, p_id, p_label):
        super(Process, self).__init__(p_id, p_label, ENTITY_TYPE_SYSTEM)
        
    def accept(self, v):
        self._accept_children(v)
        v.visit_process(self)
        
        
class Connection(object):
    def __init__(self, c_label):
        self._label = c_label
        
    def get_label(self):
        return self._label


class ContextDiagram(object):
    "main object on which the visitor will work"
    def __init__(self, process):
        self._process = process
        self.all_entities = {}
        
    def accept(self, v):
        self._process.accept(v)
        v.visit_context_diagram(self)


