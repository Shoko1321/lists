# import unittest
# from lists import Node, mylist


#************************************************************************
# Test cases Amassed to look over
#************************************************************************










# class TestmyList(unittest.TestCase):

#     def test_reverse_1(self):
#         y = []
#         x = mylist()
#         for it in range(12):
#             x.append(it)
#             y.append(it)
#         x.reverse()
#         y.reverse()
#         self.assertTrue(x == y)




#     def test_append1(self):
#         x = []
#         y= mylist()
#         x.append(1); x.append(2)
#         y.append(1); y.append(2)        
#         self.assertTrue(x == y)

#     def test_append2(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         self.assertTrue(x==y)
#     def test_pop_1(self):
#         x = []
#         y = mylist()       
#         pop_index = 27
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.pop(pop_index)
#         y.pop(pop_index)
#         self.assertTrue(x == y)

#     def test_pop_2(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.pop()
#         y.pop()
#         self.assertTrue(x == y)

#     def test_pop_3(self):
#         x = []
#         y = mylist()
#         x.append(2); y.append(4)
#         x.append(3); y.append(6)
#         x.append(4); y.append(8)
#         x.pop();y.pop()
#         self.assertFalse(x==y)

#     def test_pop4(self):
#         x = mylist()
#         x.append(1)
#         x.append(3)
#         x.append(5)
#         x.append(7)
#         x.pop(2)
#         self.assertTrue(current = 5)

#     def test_pop5(self):
#         x = mylist()
#         x.append(1)
#         x.append(3)
#         x.append(5)
#         x.append(7)
#         x.pop()
#         self.assertTrue(current = 7)

#     def test_remove_1(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.remove(1)
#         y.remove(1)
#         self.assertTrue(x==y)
#     def test_remove_2(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.remove(3)
#         y.remove(4)
#         self.assertFalse(x==y)

#     def test_remove_3(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.remove(4)
#         y.remove(4)    
#         self.assertTrue(len(x)==len(y))
#     def test_remove_4(self):
#         x = []
#         y = mylist()
#         for it in range(100):
#             x.append(it)
#             y.append(it)
#         x.remove(4)
#         y.remove(4)   
#         y.remove(0) 
#         self.assertFalse(len(x)==len(y))
        
#     def test_copy_1(self):
#         x = []
#         y = mylist()
#         for it in range(50):
#             x.append(it)
#         y = x.copy()
#         self.assertTrue(x == y)

#     def test_copy_2(self):
#         x = []
#         y = mylist()
#         x.append(2)
#         x.append(3)
#         x.append(4)
#         y = x.copy()
#         x.append(12)
#         self.assertFalse(x==y)





# if __name__ == '__main__':
#     unittest.main()