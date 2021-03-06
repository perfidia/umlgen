#!/usr/bin/env python

class SimpleVisitor(object):
    def __init__(self):
        self._visited_ids = []
        self._spaces = ""
    
    def visited(self, element):
        e_id = element.get_id()
        if self._visited_ids.count(e_id) == 0:
            self._visited_ids.append(e_id)
            return False
        
        return True
    
    def visit_context_diagram(self, context_diagram):
        print " -- context -- "
    
    def visit_process(self, process):
        print "process:", process.get_id()
        children = process.get_children()
        
        for child in children:
            print child["connection"].get_label(), "points to", child["child"].get_id()
        print "points to:"
        
    
    def visit_entity(self, entity):
        print "entity:", entity.get_id()
        children = entity.get_children()
        
        for child in children:
            print child["connection"].get_label(), "points to", child["child"].get_id()
        print "points to:"
        