#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
from umlgen.context.model import ENTITY_TYPE_HUMAN
import math

class PILVisitor(object):
    def __init__(self, size):
        self._size = size
        self._visited_ids = []
        self._image = Image.new("RGB", size, "#FFFFFF")
        self._ctx = ImageDraw.Draw(self._image)
        self._entities = {}
        self._entity_num = 0
        self._entity_positions = {}
        self._font = ImageFont.truetype("../fonts/OpenSans-Regular.ttf", 12)
        self._process_id = None
        
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
                
        for entity_id in self._entities:
            self._draw_connections(self._entities[entity_id])
            
        for entity_id in self._entities:
            if entity_id != self._process_id:
                self._draw_entity(self._entities[entity_id])
                
    def _draw_connections(self, entity):
        children = entity.get_children()
        
        from_pos = self._entity_positions[entity.get_id()]
        
        for child in children:
            to_pos = self._entity_positions[child["child"].get_id()]
            
            self._ctx.line([from_pos, to_pos], "#ABABAB", 2)
            self._ctx.text(((from_pos[0]+to_pos[0])/2+10, (from_pos[1]+to_pos[1])/2+10),
                       child["connection"].get_label(), "#121212", self._font)
            
    
    
    def visit_process(self, process):
        self._process_id = process.get_id()
        self._entity_positions[process.get_id()] = (self._size[0]/2, self._size[1]/2)
        process_size = (100, 100)
        self._ctx.ellipse(
                          (self._size[0]/2-process_size[0]/2, 
                           self._size[1]/2-process_size[1]/2,
                           self._size[0]/2+process_size[0]/2,
                           self._size[1]/2+process_size[1]/2), 
                          "#FFFFFF", "#121212")
        
        self._ctx.text((self._size[0]/2-process_size[0]/2,
                        self._size[1]/2+process_size[1]/2+10),
                       process.get_label(), "#121212", self._font)
        
        
        
    def visit_entity(self, entity):
        radius = 160
        
        pos = self._circle_pos(radius, self._entity_num, len(self._entities)-1)
        self._entity_num = self._entity_num + 1
        
        self._entity_positions[entity.get_id()] = (pos[0]+self._size[0]/2, 
                                                   pos[1]+self._size[1]/2)
        
    def _draw_entity(self, entity):
        entity_size = (80, 60)
        pos = self._entity_positions[entity.get_id()]
        
        if entity.get_type() == ENTITY_TYPE_HUMAN:
            human_actor = Image.open("../images/stick.png")
            entity_size = human_actor.size
            self._image.paste(human_actor, 
                              (int(pos[0]-entity_size[0]/2),
                               int(pos[1]-entity_size[1]/2)), 
                              human_actor)
        else:
            self._ctx.rectangle([(pos[0]-entity_size[0]/2,
                                  pos[1]-entity_size[1]/2),
                                 (pos[0]+entity_size[0]/2,
                                  pos[1]+entity_size[1]/2)], "#FFFFFF", "#121212")
            
        self._ctx.text((pos[0]-entity_size[0]/2,
                        pos[1]+entity_size[1]/2+10),
                       entity.get_label(), "#121212", self._font)
    
    def _circle_pos(self, radius, num_pos, all_pos):
        px = 0
        
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
        
        #print px
        
        if num_pos < 0.25*all_pos or num_pos > 0.75*all_pos:
            py = -py
        
        return (px, py)
        
        
        
    
    