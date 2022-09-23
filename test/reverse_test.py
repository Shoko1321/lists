import unittest
from lists import Node, mylist



class Reverse_Test(unittest.TestCase):

    def test_reverse_1(self):
        y = []
        x = mylist()
        for it in range(12):
            x.append(it)
            y.append(it)
        x.reverse()
        y.reverse()
        self.assertTrue(x == y)
