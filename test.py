import unittest
from lists import mylist
from test.append_test import Append_Test # 7 tests
from test.pop_test import Pop_Test # 6 tests
#from test.add_test import Add_Test
from test.clear_test import Clear_Test # 6 tests
from test.copy_test import Copy_Test # 7 tests
from test.count_test import Count_Test # 8 tests
#from test.extend_test import Extend_Test
from test.index_test import Index_Test # 7 tests
from test.insert_test import Insert_Test # 6 tests
#from test.mult_test import Mult_Test
from test.remove_test import Remove_Test # 10 tests
from test.reverse_test import Reverse_Test # 7 tests
from test.sort_test import Sort_Test

 










if __name__ == '__main__':
    unittest.main()
    Append_Test()
    Pop_Test()
    #Add_Test()
    Clear_Test()
    Copy_Test()
    Count_Test()
    #Extend_Test()
    Index_Test()
    Insert_Test()
    #Mult_Test()
    Remove_Test()
    Reverse_Test()
    Sort_Test()
