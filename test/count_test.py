import unittest
from lists import mylist

class Count_Test(unittest.TestCase):
    def test_count_1(self):
        a = []
        b = mylist()
        a.append(1);b.append(1)
        a.append(2);b.append(2)
        a.append(3);b.append(3)
        a.append(3);b.append(3)
        a.append(3);b.append(3)
        a.append(3);b.append(3)
        x = a.count(3)
        y = b.count(3)
        self.assertTrue(x==y)

    def test_count_2(self):
        a = []
        b = mylist()
        a.append(1);b.append(1)
        a.append(2);b.append(2)
        a.append(3);b.append(3)
        a.append(3);b.append(3)
        a.append(3);b.append(3)
        a.append(2);b.append(3)
        x = a.count(3)
        y = b.count(3)
        self.assertFalse(x==y)

    def test_count_3(self):
        a = []
        b = mylist()
        a.append("banana");b.append('banana')
        a.append('banana');b.append('banana')
        a.append('beans');b.append('beans')
        a.append('apples');b.append('apples')
        x = a.count('banana')
        y = b.count('banana')
        self.assertTrue(x==y)

    def test_count_4(self):
        a = []
        b = mylist()
        a.append("banana");b.append('banana')
        a.append('banana');b.append('banana')
        a.append('beans');b.append('beans')
        a.append('apples');b.append('apples')
        x = a.count('beans')
        y = b.count('beans')
        self.assertTrue(x==y)

    def test_count_5(self):
        a = []
        b = mylist()
        a.append("banana");b.append('banana')
        a.append('banana');b.append('banana')
        a.append('beans');b.append('beans')
        a.append('apples');b.append('apples')
        x = a.count('apples')
        y = b.count('apples')
        self.assertTrue(x==y)

    def test_count_6(self):
        a = []
        b = mylist()
        a.append("banana");b.append('banana')
        a.append('banana');b.append('banana')
        a.append(12);b.append(12)
        a.append('apples');b.append('apples')
        x = a.count(12)
        y = b.count(12)
        self.assertTrue(x==y)

    def test_count_7(self):
        a = []
        b = mylist()
        a.append("banana");b.append('banana')
        a.append('banana');b.append('banana')
        a.append('beans');b.append('banana')
        a.append('apples');b.append('apples')
        x = a.count('beans')
        y = b.count('beans')
        self.assertFalse(x==y)

    def test_count_8(self):
        a = []
        b = mylist()
        a.append("banana");b.append(1)
        a.append('banana');b.append(2)
        a.append('beans');b.append(3)
        a.append('apples');b.append('banana')
        x = a.count('banana')
        y = b.count('banana')
        self.assertFalse(x==y)