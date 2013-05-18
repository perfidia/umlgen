#!/usr/bin/env python

import xml.etree.ElementTree as ET
from model import *

class XMLReader(object):
    def __init__(self, path):
        self._path = path
        self._tree = ET.parse(path)
        
    def create_graph(self):
        root = self._tree.getroot()
        p = self._get_process(root)
        entities = self._get_entities(root)
        entities[p.get_id()] = p
        self._make_connections(root, entities)
        c = ContextDiagram(p)
        c.all_entities = entities
        
        return c
    
    def _make_connections(self, root, entities):
        connections_tag = root.find("connections")
        
        for tag in connections_tag.findall("connection"):
            label = ""
            try:
                label = tag.find("label").text.strip()
            except:
                pass
            c_from = tag.find("from").text.strip()
            c_to = tag.find("to").text.strip()
            conn = Connection(label)
            
            entities[c_from].add_child(entities[c_to], conn)
    
    def _get_entities(self, root):
        entities_tag = root.find("entities")
        entities = {}
        
        for tag in entities_tag.findall("entity"):
            label = ""
            try:
                label = tag.find("label").text.strip()
            except:
                pass
            eid = tag.find("id").text.strip()
            
            etype = "system"
            try:
                etype = tag.find("type").text.strip()
            except:
                pass
            
            e_type = ENTITY_TYPE_SYSTEM
            if etype == "human":
                e_type = ENTITY_TYPE_HUMAN
            
            entity = Entity(eid, label, e_type)
            
            entities[eid] = entity
            
        return entities
    
    def _get_process(self, root):
        tag = root.find("process")
        label = ""
        try:
            label = tag.find("label").text.strip()
        except:
            pass
        pid = tag.find("id").text.strip()
        return Process(pid, label)
    