import unittest
from lists import mylist

class Index_Test(unittest.TestCase):
    def test_index_1(self):
        a = []
        b = mylist()
        a.append(1); a.append(2);a.append(3)
        b.append(1); b.append(2);b.append(3)
        x = a.index(1)
        y = b.index(1)
        self.assertTrue(x==y)
        
    def test_index_2(self):
        a = []
        b = mylist()
        a.append('apple'); a.append('cherry');a.append('banana')
        b.append('apple'); b.append('cherry');b.append('banana')
        x = a.index('cherry')
        y = b.index('cherry')
        self.assertTrue(x==y)

    def test_index_3(self):
        a = []
        b = mylist()
        a.append(1); a.append(2);a.append(3)
        b.append(1); b.append(1);b.append(1)
        x = a.index(1)
        y = b.index(1)
        self.assertTrue(x==y)

    def test_index_4(self):
        a = []
        b = mylist()
        a.append('beans'); a.append(2);a.append('stale bread')
        b.append(-30); b.append('beans');b.append(3)
        x = a.index(2)
        y = b.index('beans')
        self.assertTrue(x==y)

    def test_index_5(self):
        a = []
        b = mylist()
        a.append('beans'); a.append(2);a.append('stale bread')
        b.append(-30); b.append('beans');b.append(3)
        x = a.index('beans')
        y = b.index('beans')
        self.assertFalse(x==y)

    def test_index_6(self):
        a = []
        b = mylist()
        a.append('beans'); a.append(2);a.append('stale bread');a.append('4th element')
        b.append(-30); b.append('beans');b.append(3)
        x = a.index('4th element')
        y = b.index(3)
        self.assertFalse(x==y)

    def test_index_7(self):
        a = []
        b = mylist()
        a.append('beans'); a.append(2);a.append('stale bread');a.append('4th element')
        b.append(-30); b.append('beans');b.append(3);b.append(0)
        x = a.index('4th element')
        y = b.index(0)
        self.assertTrue(x==y)