from lists import mylist, Node

import unittest
from lists import mylist

class Clear_Test(unittest.TestCase):
    def test_clear_1(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        x.clear
        y.clear
        self.assertTrue(x==y)

    def test_clear_2(self):
        x = []
        y = mylist()
        x.append("beans")
        y.append("beans")
        x.clear()
        y.clear()
        self.assertTrue(x==y)

    def test_clear_3(self):
        x = []
        y = mylist()
        x.append("beans")
        y.append(27)
        x.clear()
        y.clear()
        self.assertTrue(x==y)
    def test_clear_4(self):
        x = []
        y = mylist()
        x.append("beans")
        y.append("beans")
        self.assertTrue(x==y)
        x.append("I")
        x.append("Like")
        x.append("beans")
        y.append("I")
        y.append("Like")
        y.append("beans")
        x.clear()
        y.clear()
        self.assertTrue(x==y)

    def test_clear_5(self):
        x = []
        y = mylist()
        x.append("string")
        y.append("string")
        x.append(12)
        y.append(12)
        x.append("13")
        y.append("13")
        x.clear()
        y.clear()
        self.assertTrue(x==y)

    def test_clear_6(self):
        x = []
        y = mylist()
        x.append("string")
        y.append("string")
        x.append(22)
        y.append(12)
        x.append("13")
        y.append("13")
        self.assertFalse(x==y)
        x.clear()
        y.clear()
        self.assertTrue(x==y)
