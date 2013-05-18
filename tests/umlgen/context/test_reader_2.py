'''
Created on May 8, 2013

@author: matkra
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
        path.append('example1.xml')
        
        self.reader = XMLReader(os.sep.join(path))
        self.diagram = self.reader.create_graph()


    def testEntitiesId(self):
        temp = {}
        temp[0]="account1"
        temp[1]="server"
        temp[2]="account2"
        temp[3]="database2"
        temp[4]="p_0"
        temp[5]="database1"
        i=0
        for entity in self.diagram.all_entities:
            self.assertEqual(entity, temp[i])
            i+=1
            
    def testConnectionEntities(self):
        i = 0
        temp = {}
        temp[0]="account1"
        temp[1]="account2"
        temp[2]="p_0"
        temp[3]="p_0"
        temp[4]="p_0"
        for entity_id in self.diagram.all_entities:
            entity = self.diagram.all_entities[entity_id]
            children = entity.get_children()
            temp1 = {}
            temp1[0] = "p_0"
            temp1[1] = "p_0"
            temp1[2] = "server"
            temp1[3] = "database1"
            temp1[4] = "database2" 
            
            for entityid in children:
                self.assertEquals(entity_id, temp[i])
                self.assertEquals(entityid.get("child").get_id(), temp1[i])
                i+=1
                
    def testProcessLabel(self):
            self.assertEqual(self.diagram._process.get_label(), "system")
            
    def testProcessId(self):
        self.assertEqual(self.diagram._process.get_id(), "p_0")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()