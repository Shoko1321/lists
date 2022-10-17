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

    def test_remove_5(self):
        x = []
        y = mylist()
        x.append(1);x.append(2);x.append(3);x.append(4);x.append(5)
        y.append(1);y.append(2);y.append(3);y.append(4);y.append(5)
        x.remove(2)
        y.remove(2)
        x.remove(1)
        y.remove(1)
        x.remove(3)
        y.remove(3)
        self.assertTrue(x==y)

    def test_remove_6(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(4);x.remove(7);x.remove(29)
        y.remove(4);y.remove(7);y.remove(29)
           
        self.assertTrue(len(x)==len(y))

    def test_remove_7(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.remove(4);x.remove(7);x.remove(29)
        y.remove(4);y.remove(7);y.remove(29)
        self.assertTrue(x==y)        

    def test_remove_8(self):
        x = []
        y = mylist()
        x.append('string');x.append(69);x.append('words')
        y.append('string');y.append(69);y.append('words')
        x.remove('string')
        y.remove('string')
        self.assertTrue(x==y)

    def test_remove_9(self):
        x = []
        y = mylist()
        x.append('string');x.append(69);x.append('words')
        y.append('string');y.append(69);y.append('words')
        x.remove('string')
        y.remove('string')
        x.remove(69)
        y.remove(69)
        self.assertTrue(x==y)

    def test_remove_10(self):
        x = []
        y = mylist()
        x.append('string');x.append(69);x.append('words')
        y.append('string');y.append(69);y.append('words')
        x.remove('string')
        y.remove('string')
        x.remove(69)
        y.remove(69)
        x.remove('words')
        y.remove('words')
        self.assertTrue(x==y)