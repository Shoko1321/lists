import unittest
from lists import mylist

class Add_Test(unittest.TestCase):
    def test_add_1(self):
        x = []
        q = []
        y = mylist()
        x.append('one'); x.append('two')
        y.append('one'); y.append('two')
        q.append('one'); q.append('two')     
        x = q + x
        y + y
        self.assertTrue(x == y)
   
