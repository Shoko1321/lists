import unittest
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
        
        print(x,y,z)
