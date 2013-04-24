#!/usr/bin/env python

from PIL import Image, ImageDraw
import math

class PILVisitor(object):
    def __init__(self, size):
        self._size = size
        self._visited_ids = []
        self._image = Image.new("RGB", size, "#FFFFFF")
        self._ctx = ImageDraw.Draw(self._image)
        self._entities = {}
        self._entity_num = 0
        
    def save(self, path):
        self._image.save(path)
        
    def visited(self, element):
        e_id = element.get_id()
        if self._visited_ids.count(e_id) == 0:
            self._visited_ids.append(e_id)
            return False
        
        return True
    
    
    def visit_context_diagram(self, context_diagram):
        self._entities = context_diagram.all_entities
        
        for entity_id in self._entities:
            if not self.visited(self._entities[entity_id]):
                self._entities[entity_id].accept(self)
    
    
    def visit_process(self, process):
        process_size = (100, 100)
        self._ctx.ellipse(
                          (self._size[0]/2-process_size[0]/2, 
                           self._size[1]/2-process_size[1]/2,
                           self._size[0]/2+process_size[0]/2,
                           self._size[1]/2+process_size[1]/2), 
                          "#FF0000")
        
        
    def visit_entity(self, entity):
        print entity.get_id()
        radius = 160
        entity_size = (80, 60)
        pos = self._circle_pos(radius, self._entity_num, len(self._entities)-1)
        self._entity_num = self._entity_num + 1
        self._ctx.rectangle([(pos[0]+self._size[0]/2-entity_size[0]/2,
                              pos[1]+self._size[1]/2-entity_size[1]/2),
                             (pos[0]+self._size[0]/2+entity_size[0]/2,
                              pos[1]+self._size[1]/2+entity_size[1]/2)], "#00FF00")
    
    def _circle_pos(self, radius, num_pos, all_pos):
        px = 0
        py = 0
        
        if num_pos < 0.25*all_pos:
            #print "one", num_pos, all_pos
            px = -4*radius*float(num_pos)/float(all_pos)
        
        elif num_pos < 0.5*all_pos:
            #print "two", num_pos, all_pos
            px = -4*radius*float(0.5*all_pos-num_pos)/float(all_pos)
            
        elif num_pos < 0.75*all_pos:
            #print "three", num_pos, all_pos
            px = 4*radius*float(num_pos - 0.5*all_pos)/float(all_pos)
            
        else:
            #print "four", num_pos, all_pos
            px = 4*radius*float(all_pos-num_pos)/float(all_pos)
            
        val = radius*radius-px*px
        if val < 0:
            val = 0
        py = math.sqrt(val)
        
        print px
        
        if num_pos < 0.25*all_pos or num_pos > 0.75*all_pos:
            py = -py
        
        return (px, py)
        
        
        
    
    