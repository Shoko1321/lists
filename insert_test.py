import unittest
from lists import mylist

class Insert_Test(unittest.TestCase):
    def test_insert1(self):
        x = []
        y= mylist()
        x.append('a'); x.append('b')
        y.append('a'); y.append('b')    
        x.insert(0,'c')
        y.insert(0,'c')     
        self.assertTrue(x == y)


if __name__ == '__main__':
    unittest.main()