import unittest
from lists import mylist

class Insert_Test(unittest.TestCase):
    def test_insert_1(self):
        x = []
        y= mylist()
        x.append('a'); x.append('b')
        y.append('a'); y.append('b')    
        x.insert(0,'c')
        y.insert(0,'c')     
        self.assertTrue(x == y)

    def test_insert_2(self):
        x = []
        y= mylist()
        x.insert(0,'c')
        y.insert(0,'c')     
        self.assertTrue(x == y)

    def test_insert_3(self):
        x = []
        y= mylist()
        x.append('c'); x.append('b')
        y.append('b');y.append(12)
        x.insert(2,12)
        y.insert(0,'c')     
        self.assertTrue(x == y)

    def test_insert_4(self):
        x = []
        y= mylist()
        x.append('c'); x.append('b');y.append('false')
        y.append('b');y.append(12)
        x.insert(2,12)
        y.insert(0,'c')     
        self.assertFalse(x == y)

    def test_insert_5(self):
        x = []
        y= mylist()
        x.append('c'); x.append('b')
        y.append('b');y.append(12)
        x.insert(2,12)
        y.insert(0,'c')   
        x.insert(1,'insert1')
        y.insert(1,'insert1')  
        self.assertTrue(x == y)

    def test_insert_6(self):
        x = []
        y= mylist()
        x.insert(0,'c');x.insert(0,'b');x.insert(0,'a')
        y.insert(0,'c');y.insert(0,'b');y.insert(0,'a')
        self.assertTrue(x == y)