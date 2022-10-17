import unittest
from lists import Node, mylist



class Reverse_Test(unittest.TestCase):

    def test_reverse_1(self):
        y = []
        x = mylist()
        for it in range(10):
            x.append(it)
            y.append(it)
        x.reverse()
        y.reverse()
        self.assertTrue(x == y)

    def test_reverse_2(self):
        y = []
        x = mylist()
        for it in range(20):
            x.append(it)
            y.append(it)
        x.reverse()
        y.reverse()
        self.assertTrue(x == y)
        
    def test_reverse_3(self):
        x = []
        y = mylist()
        x.append('beans');x.append('bacon');x.append('whiskey');x.append('lard')
        y.append('beans');y.append('bacon');y.append('whiskey');y.append('lard')
        x.reverse()
        y.reverse()
        self.assertTrue(x==y)

    def test_reverse_4(self):
        x = []
        y = mylist()
        for it in range(5):
            x.append(it)
            y.append(it)
        x.append('string')
        y.append('string')
        x.reverse();y.reverse()
        self.assertTrue(x==y)

    def test_reverse_5(self):
        x = []
        y = mylist()
        for it in range(5):
            x.append(it)
            y.append(it)
        x.append('string')
        y.append('beans')
        x.reverse();y.reverse()
        self.assertFalse(x==y)

    def test_reverse_6(self):
        y = []
        x = mylist()
        for it in range(20):
            x.append(it)
            y.append(it)
        x.reverse()
        self.assertFalse(x == y)

    def test_reverse_7(self):
        y = []
        x = mylist()
        for it in range(20):
            x.append(it)
            y.append(it)
        y.reverse()
        self.assertFalse(x == y)