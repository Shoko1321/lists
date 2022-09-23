import unittest
from lists import mylist, Node


class Pop_Test(unittest.TestCase):
    def test_pop_1(self):
        x = []
        y = mylist()       
        pop_index = 27
        for it in range(100):
            x.append(it)
            y.append(it)
        x.pop(pop_index)
        y.pop(pop_index)
        self.assertTrue(x == y)

    def test_pop_2(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.pop()
        y.pop()
        self.assertTrue(x == y)

    def test_pop_3(self):
        x = []
        y = mylist()
        x.append(2); y.append(4)
        x.append(3); y.append(6)
        x.append(4); y.append(8)
        x.pop();y.pop()
        self.assertFalse(x==y)