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
    
    def test_sort_2(self):
        x = []
        y = mylist()
        x.append('ab');x.append('a');x.append('abc')
        y.append('ab');y.append('a');y.append('abc')
        self.assertTrue(x==y)

    def test_sort_3(self):
        x = mylist()
        y = mylist()
        x.append(25);x.append(-25);x.append(2)
        y.append(-25,);y.append(2);y.append(25)
        x.sort()
        self.assertTrue(x==y)

    def test_sort_4(self):
        x = mylist()
        y = mylist()
        x.append('Ford');x.append('BMW');x.append('Volvo')
        y.append('BMW');y.append('Ford');y.append('Volvo')
        x.sort()
        self.assertTrue(x==y)

    def test_sort_5(self):
        x = mylist()
        y = mylist()
        x.append(25);x.append(-25);x.append(2)
        y.append(25,);y.append(2);y.append(-25)
        x.sort()
        self.assertFalse(x==y)

    def test_sort_6(self):
        x = mylist()
        y = mylist()
        x.append(7);x.append(86);x.append(4000000002)
        y.append(-25,);y.append(2);y.append(25)
        x.sort()
        y.sort()
        self.assertFalse(x==y)

    def test_sort_7(self):
        x = []
        y = mylist()
        x.append(7);x.append(86);x.append(4000000002)
        y.append(-25,);y.append(2);y.append(25)
        x.sort()
        y.sort()
        self.assertFalse(x==y)

    # def test_sort_8(self):
    #     x = mylist()
    #     y = mylist()
    #     x.append('7');x.append(86);x.append(4000000002)
    #     y.append(-25,);y.append(2);y.append(25)
    #     x.sort()
    #     y.sort()
    #     self.assertRaises(TypeError)
