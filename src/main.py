#!/usr/bin/env python

from umlgen import *

def main():
    r = XMLReader("../context/example.xml")
    context = r.create_graph()
    
    v = PILVisitor((800, 500))
    context.accept(v)
    v.save("path.png")
    
    return

if __name__ == "__main__":
    main()
    