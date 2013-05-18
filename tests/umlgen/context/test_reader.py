'''
Created on Apr 24, 2013

@author: Mateusz Krawczynski
'''
import unittest
from umlgen import XMLReader
import os

class Test(unittest.TestCase):


    def setUp(self):
        path = os.getcwd().split(os.sep)
        previous = ''

        for d in reversed(path[:]):
            if not (d == 'umlgen' and previous != 'context'):
                previous = path.pop()
                continue

            break

        path.append('samples')
        path.append('context')
        path.append('example0.xml')
        
        self.reader = XMLReader(os.sep.join(path))
        self.diagram = self.reader.create_graph()



    def testEntitiesId(self):
        temp = {}
        temp[0] = "0"
        temp[1] = "e_1"
        temp[2] = "p_0"
        temp[3] = "e_2"
        i = 0
        for entity in self.diagram.all_entities:
            self.assertEqual(entity, temp[i])
            i+=1

    def testConnections(self):
        for entity_id in self.diagram.all_entities:
            entity = self.diagram.all_entities[entity_id]
            children = entity.get_children()
            for entityid in children:
                self.assertEqual(entityid.get("connection").get_label(), "a connection")
                
    def testConnectionEntities(self):
        for entity_id in self.diagram.all_entities:
            entity = self.diagram.all_entities[entity_id]
            children = entity.get_children()
            temp = {}
            temp[0] = "e_1"
            temp[1] = "0"
            i = 0
            for entityid in children:
                self.assertEquals(entityid.get("child").get_id(), temp[i])
                i+=1
             
            
    def testProcessLabel(self):
            self.assertEqual(self.diagram._process.get_label(), "system")
            
    def testProcessId(self):
        self.assertEqual(self.diagram._process.get_id(), "p_0")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()