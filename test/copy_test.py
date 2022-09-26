import unittest
from lists import Node, mylist

class Copy_Test(unittest.TestCase):
    
    def test_copy_1(self):
        x = []
        y = mylist()
        for it in range(50):
            x.append(it)
        y = x.copy()
        self.assertTrue(x == y)

    def test_copy_2(self):
        x = []
        y = mylist()
        x.append(2)
        x.append(3)
        x.append(4)
        y = x.copy()
        x.append(12)
        self.assertFalse(x==y)