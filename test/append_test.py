import unittest
from lists import mylist

class Append_Test(unittest.TestCase):
    def test_append1(self):
        x = []
        y= mylist()
        x.append(1); x.append(2)
        y.append(1); y.append(2)        
        self.assertTrue(x == y)

    def test_append2(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        self.assertTrue(x==y)