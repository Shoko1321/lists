





from configparser import InterpolationSyntaxError


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

    def __str__(self):
        return "Node(" + str(self.data) + ")"
    __repr__ = __str__


# # create an iterator object from that iterable
# iter_obj = iter(iterable)

# # infinite loop
# while True:
#     try:
#         # get the next item
#         element = next(iter_obj)
#         # do something with element
#     except StopIteration:
#         # if StopIteration is raised, break from loop
#         break



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

    def __radd__(self,other):#Should work?
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __add__(self,other):# needs work
        new_list = mylist + other
        return new_list [mylist,other]

    

    def __mult__(self,other):
        return data(self.value * other.value)

    def __eq__(self, other):
        if len(self) != len(other): return False
        for it in range(len(self)):
            if self[it] != other[it]: return False
        return True
        

    def append(self,data):
        new_node = Node(data = data)
        if self.head is None:
            self.head = new_node  
        else:
            last = self.head
            while (last.next != None):
                last = last.next
            last.next = new_node
            
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

                
            
        
    def sort(self):#wip
        current = self.head
        index = None
        if(self.head == None):
            return
        else:
            while(current != None):
                index = current.next
                while(index != None):
                    if(current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
            


        

            

        


 
 


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

            
    def extend(self):
        pass



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
    y = []

    
 
    x.append(27)
    y.append(27)
    x.append(-15)
    y.append(-15)
    x.append(69)
    y.append(69)
    print(x,y)
    x.sort()
    y.sort()

    
    print(x,y)


    


    # print(x,y)
    # x.sort()
    # y.sort()
    
    # x.clear()
    # y.clear()
    # print(x,y)
    # print(x.count(3))
    # print(y.count(3))
    # print(x.copy())
    # print(y.copy())
    # print(x,y)
    # x.append(x)   x.copy(z)     x.extend(x)    x.insert(x)    x.remove(x)  
    # x.sort(x)  x.clear(x)    x.count(     x.index(x)     x.pop(x) 
    # x.reverse(x)

    # as a function
    # linked list
