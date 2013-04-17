#!/usr/bin/env python

from umlgen import *

def main():
    entity_1 = Entity("id_1", "one", ENTITY_TYPE_HUMAN)
    entity_2 = Entity("id_2", "two", ENTITY_TYPE_SYSTEM)
    
    process = Process("p_id", "label")
    process.add_child(entity_1)
    process.add_child(entity_2)
    
    entity_1.add_child(entity_2)
    entity_2.add_child(entity_1)
    
    context = ContextDiagram(process)
    
    v = SimpleVisitor()
    context.accept(v)
    
    return

if __name__ == "__main__":
    main()
    