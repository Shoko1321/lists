import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "Node(" + str(self.data) + ")"
    __repr__ = __str__
class mylist:
    def __init__(self):
        self.head = None
        self.tail = None
       
    def __getitem__(self, index):
        counter = 0
        current = self.head
        while current != None:
            if index == counter:
                return current.data
            counter +=1  
            current = current.next
        raise IndexError
                
    def __str__(self):
        ret = '<'
        cur = self.head
        while cur != None:
            ret += str(cur.data)
            cur = cur.next
            ret += ', '
        return ret[:-1] + '>'
    __repr__ = __str__

    def __len__(self):
        counter = 0
        current = self.head
        while current != None:
            current = current.next
            counter += 1
        return counter

    def __iter__(self):#halp
        curNode = self.head
        while curNode:
            yield curNode.data
            curNode = curNode.next



    def __add__(self,other):
        for x in other:
            self.append(x)
        return self

    def __mul__(self,other):
        count = 0
        while count != other:
            count += 1
            self.extend(self)
        return self

    def __eq__(self, other):
        if len(self) != len(other): return False
        for it in range(len(self)):
            if self[it] != other[it]: return False
        return True

    def append(self,data):
        new_node = Node(data = data)
        print('check 1')
        if self.head is None:
            self.head = new_node  
        else:
            last = self.head
            print('check2')
            while (last.next != None):
                print(self)
                last = last.next
            last.next = new_node
            breakpoint()
            print('check4')

    def pop(self,position=None):
        if self.head is None:
            raise IndexError
        if position is None:
            position = len(self)-1
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
        print(f'{current.data} was popped')

    def sort(self):#type error if both int and string in list, auto raises same error as built in function
        cur = self.head
        index = None
        if(self.head == None):
            return
        else:
            while(cur != None):
                index = cur.next
                while(index != None):
                    if(cur.data > index.data):
                        temp = cur.data
                        cur.data = index.data
                        index.data = temp
                    index = index.next
                cur = cur.next

    def index(self,data):
        current = self.head
        count = 0
        while (current):
            if(current.data == data):
                return count
            count +=1
            current = current.next
        raise ValueError

    def reverse(self):
        prev = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def clear(self):
       self.head = None

    def count(self,intake):
        current = self.head
        count = 0
        while(current is not None):
            if current.data == intake:
                count += 1
            current = current.next
        return count

    def copy(self):
        current = self.head
        newList = None
        tail = None
        while current:
            if newList is None:
                newList = Node(current.data, None)
                tail = newList
            else:
                tail.next = Node()
                tail = tail.next
                tail.data = current.data
                tail.next = None
            current = current.next
        return newList

    def extend(self,list_to_add):# cant extend a list if an item is a string of multiple characters
        list_to_add = copy.deepcopy(list_to_add)
        for y in list_to_add:
            self.append(y)

    def insert(self,position,data):
        if (position == 0):
            n = Node(data = data)
            n.next = self.head
            self.head = n
        elif position >= len(self):
            n = Node(data = data)
            last = self.head
            while(last.next):
                last = last.next
            last.next = n
        else:
            if position != 0:
                n = Node(data = data)
                index_track = 0
                cur = self.head
                while index_track != position -1:
                    cur = self.head.next
                    index_track +=1
                if index_track == position -1:
                    n = Node(data = data)
                    prev_node = cur
                    next_node = cur.next
                    prev_node . next = n
                    n.next = next_node
    def remove(self,element):
        temp = self.head
        if(temp is not None):
            if (temp.data == element):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == element:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            raise ValueError
        prev.next = temp.next
        temp = None




        
if __name__ == '__main__':
    node1 = Node(data= 0)
    node2 = Node(data= 0)
    x = mylist() 
    z = mylist()
    y = []
   
    
 
    x.append('one')
    y.append('4')
    x.append('two')
    y.append('5')
    x.append('three')
    y.append('6')    
    z.append('i have no idea')
    x.extend(x)
    print(x) 

    # tests cases for add mul extend. Infinite loop caused by append?(recursion possibly?)




