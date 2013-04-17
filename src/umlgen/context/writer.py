#!/usr/bin/env python

from PIL import *

class PILWriter(object):
    """
    The PILWriter object will work
    with a visitor - the visitor will
    generate a PIL image, and the writers
    task is to write the image to a specific path,
    with a specific format
    """
    def __init__(self, path):
        self._path
    
    