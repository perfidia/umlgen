#!/usr/bin/env python

from umlgen import *

def main():
    r = XMLReader("../context/example.xml")
    context = r.create_graph()
    
    v = SimpleVisitor()
    context.accept(v)
    
    return

if __name__ == "__main__":
    main()
    