UMLGen
======

Description
-----------

UMLGen is a set of tools for generating a variety of UML diagram types from XML files. Right now there are two tools: one for context diagrams
and second for state diagrams.

Installation
------------

### Simple

    python setup.py install

### Using eggs

    python setup.py bdist_egg
    cd dist
    easy_install <package_name>

Getting started
---------------

To use the context diagram tool you need to have PIL with TTF support installed

The context diagram tool can be found in the folder src under the name of umlgen-context. When you type `umlgen-context --help` you will see
the following options:
* -c FILE, to specify a config file to use
* -o OUTPUT to specify an output file to use
* -x WIDTH to specify the width of the output image
* -y HEIGHT to specify the height of the output image
* -m MULTIPLIER to specify how big we want the UML object on the image to be (0.5 means half the original size, 2.0 means two times as big)

so, to see an example usage, type:

`umlgen-context -c ../context/example2.xml -o output.png`

Just play around to get used to it.

Context diagram xml
-------------------

The context/example.xml file is commented so that you can quickly start creating your own context diagrams, the elements of the xml:
* context is the root node and must always be in the xml config file
* process is the main entity which other entities will graphically circle around
* entities can have many entity nodes, every entity consists of the id, label and type (process is an entity with type=system)
* connections can have many connection nodes, a connection consists of a from node which must be one of the available IDs, to node - the same situation and a connection label node

Now you can start creating your own diagrams!


Authors
-------

See AUTHORS file.

License
-------

UMLGen is released under The MIT License. See LICENSE file.
