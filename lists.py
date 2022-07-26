from ast import While
import pdb
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "Node(" + str(self.data) + ")"
    __repr__ = __str__


node1 = Node(data= 5)
node2 = Node(data= 3)



class mylist:
    def __init__(self):
        self.head = None

    def append(self,data):
        self.head = Node(data = data)
    def __str__(self):

        ret = '( '
        cur = self.head
        while cur != None:
            ret += str(cur.data)
            cur = cur.next

        ret += ')'
        return ret
    __repr__ = __str__
    def clear(self):
        pass
templist = mylist()
templist.append(data=70)
print(templist)

# x.append(    x.copy()     x.extend(    x.insert(    x.remove(    x.sort(
# x.clear()    x.count(     x.index(     x.pop(       x.reverse()
# as a function
# linked list
