import unittest
from lists import mylist

class Append_Test(unittest.TestCase):
    def test_append_1(self):
        x = []
        y= mylist()
        x.append(1); x.append(2)
        y.append(1); y.append(2)        
        self.assertTrue(x == y)

    def test_append_2(self):
        x = []
        y= mylist()
        x.append(1); x.append(2)
        y.append(1); y.append(75)        
        self.assertFalse(x == y)

    def test_append_3(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it)
        self.assertTrue(x==y)

    def test_append_4(self):
        x = []
        y = mylist()
        for it in range(100):
            x.append(it)
            y.append(it);y.append(it)
        self.assertFalse(x==y)

    def test_append_5(self):
        x = []
        y = mylist()
        x.append(17); y.append(17)
        x.append("thirty-seven");y.append("thirty-seven")
        x.append("well, thats a string and a integer");y.append("well, thats a string and a integer")
        x.append(-25);y.append(-25)
        self.assertTrue(x==y)

    def test_append_6(self):
        x = []
        y = mylist()
        z = ["list of extra things",69, "j0e_the_r0ck"]
        x.append("I miss Halo");y.append("I miss Halo")
        x.append(17);y.append(17)
        x.append(z);y.append(z)
        self.assertTrue(x==y)

    def test_append_7(self):
        x = []
        y = mylist()
        z = ["list of extra things",69, "j0e_the_r0ck"]
        x.append("I miss Halo");y.append("I miss Halo")
        x.append(17);y.append(18)
        x.append(z);y.append(z)
        self.assertFalse(x==y)