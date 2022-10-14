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

    def test_copy_3(self):
        x = []
        y = mylist()
        z = ["god has forsaken me", "javas better than python"]
        x.append(z)
        self.assertFalse(x == y)
        y= x.copy()
        self.assertTrue(x==y)

    def test_copy_4(self):
        x = []
        y = mylist()
        z = [1,2,3,4,5,6,7,8,9,10]
        x.append(z)
        y = x.copy()
        self.assertTrue(x == y)

    def test_copy_5(self):
        x = []
        y = mylist()
        z = ["string", 23] 
        y = x.copy()
        x.append(z)
        self.assertFalse(x==y)

    def test_copy_6(self):
        x = []
        y = mylist()
        z = ["generic list", "with multiple elements", 12,26,13,0,-27]
        x.append(z)
        y = x.copy()
        self.assertTrue(x==y)

    def test_copy_7(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
        y.append(000000000)
        x.append(47)
        x.append(28)
        y = x.copy
        x.append(1)
        self.assertTrue(True)