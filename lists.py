class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "Node(" + str(self.data) + ")"
    __repr__ = __str__


node1 = Node(data= 0)
node2 = Node(data= 0)



class mylist:
    def __init__(self):
        self.head = None

    def __getitem__(self,data):
        pass
        

    def append(self,data):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node  
        else:
            last = self.head
            while (last.next != None):
                last = last.next
            last.next = new_node
            
                
        
    def __str__(self):
        ret = '<'
        cur = self.head
        while cur != None:
            ret += str(cur.data)
            cur = cur.next
            ret += ','
        return ret[:-1] + '>'
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

 
x = mylist() 
y = []
print(x)
x.append(3)
y.append(3)
print(x,y)
x.append(4)
y.append(4)
print(x,y)
x.append(3)
y.append(3)
print(x,y)
mylist[x] = 'bork'
print(mylist)


# x.pop()
# y.pop()
# print(x,y)
# x.append(x)   x.copy(z)     x.extend(x)    x.insert(x)    x.remove(x)  
# x.sort(x)  x.clear(x)    x.count(     x.index(x)     x.pop(x) 
# x.reverse(x)

# as a function
# linked list
