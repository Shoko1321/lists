import unittest
from lists import mylist



class Sort_Test(unittest.TestCase):
    def test_sort_1(self):
        x = []
        y = mylist()
        x.append(3);x.append(47);x.append(1)
        y.append(3);y.append(47);y.append(1)
        x.sort()
        y.sort()
        self.assertTrue(x==y)
  
  