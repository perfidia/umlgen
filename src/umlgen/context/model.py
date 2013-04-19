# -*- coding: utf-8 -*-

ENTITY_TYPE_SYSTEM = 1
ENTITY_TYPE_HUMAN = 2

class Entity(object):
    def __init__(self, id, label, type):
        self.id = id
        self.label = label
        self.type = type
        self.children = []

    def append(self, child, connection):
        self.children.append({ "child": child, "connection": connection })

class Process(Entity):
    def __init__(self, id, label):
        super(Process, self).__init__(id, label, ENTITY_TYPE_SYSTEM)

class Connection(object):
    def __init__(self, label):
        self.label = label

class ContextDiagram(object):
    "main object on which the visitor will work"
    def __init__(self, process):
        self._process = process
