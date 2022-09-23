import unittest
from lists import Node, mylist

class Remove_Test(unittest.TestCase):
    def test_remove_1(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(1)
        y.remove(1)
        self.assertTrue(x==y)
    def test_remove_2(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(3)
        y.remove(4)
        self.assertFalse(x==y)

    def test_remove_3(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(4)
        y.remove(4)    
        self.assertTrue(len(x)==len(y))
    def test_remove_4(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(4)
        y.remove(4)   
        y.remove(0) 
        self.assertFalse(len(x)==len(y))