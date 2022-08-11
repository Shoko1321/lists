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
    def pop(self):
        pass
    def copy(self):
        pass
    def extend(self):
        pass
    def insert(self):
        pass
    def remove(self):
        pass
    def sort(self):
        pass
    def count(self):
        pass
    def index(self):
        pass
    def reverse(self):
        pass


templist = mylist()
templist.append(data=70)
print(templist)

# x.append(x)   x.copy(z)     x.extend(x)    x.insert(x)    x.remove(x)  
# x.sort(x)  x.clear(x)    x.count(     x.index(x)     x.pop(x) 
# x.reverse(x)

# as a function
# linked list
