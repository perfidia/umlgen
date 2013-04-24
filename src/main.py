#!/usr/bin/env python

from umlgen import *
from optparse import OptionParser
import sys

def main():
    parser = OptionParser()
    parser.add_option("-c", "--conf", help="input file in XML format", dest="conf")
    parser.add_option("-o", "--output", help="place where to generate output file (default is ./output.png)", dest="output")
    
    if len(sys.argv) < 2:
        parser.print_help()
        return
        
    options = {}
    (options, args) = parser.parse_args()
        
    if options.output == None:
        options.output = "./output.png"
            
    r = XMLReader(options.conf)
    context = r.create_graph()
    
    v = PILVisitor((800, 500))
    context.accept(v)
    v.save(options.output)
    
    return

if __name__ == "__main__":
    main()
    