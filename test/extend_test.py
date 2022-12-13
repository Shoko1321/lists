import unittest
import random
import string
from lists import mylist

class Extend_Test(unittest.TestCase):
    def test_extend_1(self):
        x = []
        y = mylist()
        z = []
        x.append(1);x.append(2)
        y.append(3);y.append(4)
        z.append(1);z.append(2);z.append(3);z.append(4)
        x.extend(y)
        print(x,y)#see if joe reads my code
        self.assertTrue(x == z)

    def test_extend_2(self):
        x = []
        y = mylist()
        x.append(1)
        x.extend(x)
        y.append(1)
        y.extend(y)
        self.assertTrue(x == y)

    def test_extend_3(self):
        x = []
        y = mylist()
        for it in range(5**6):
            rando = random.choice(string.ascii_letters)
            x.append(rando)
            y.append(rando)
            
        self.assertTrue(x == y)

        

