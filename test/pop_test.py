import unittest
from lists import mylist, Node
import random


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

    def test_pop_4(self):
        x = mylist()
        y = []
        x.append(6); 
        x.append(2)
        x.append(3)
        x.pop()
        self.assertTrue(current.data == 3)


    def test_pop_5(self):
        x = mylist()
        y = []
        x.append(12); y.append(12)
        x.append(27); y.append(27)
        x.append(2); y.append(2)
        x.append(-27); y.append(-27)
        x.pop(3); y.pop(3)
        self.assertTrue( x == y)

    def test_pop_6(self):
        x = mylist()
        y = []
        while len(x) <=10:
            random_num = random.randint(0,50)
            x.append(random_num); y.append(random_num)
            index_selected = random.randint(1,10)
        x.pop(index_selected); y.pop(index_selected)
        self.assertTrue(x == y)

    def test_pop_7(self):
        x = mylist()
        x.pop()
        self.assertRaises(IndexError)