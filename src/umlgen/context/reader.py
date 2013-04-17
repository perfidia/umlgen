#!/usr/bin/env python

from xml.dom import minidom

class XMLReader(object):
    def __init__(self, path):
        self._path = path
        
    def create_graph(self):
        return None