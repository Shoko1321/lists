# multiplication add, not = , 
# pop doesnt return last element, sort doesnt work, refactor clear, 
# extend, tests for everything
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail = data

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
            ret += ','
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


    def __add__(self,first,second):
        curr1 = self.reverse(first)
        curr2 = self.reverse(second)

        sum = 0
        carry = 0
        res = None
        prev = None

        while curr1 is not None or curr2 is not None:
            sum = carry + (curr1.data if curr1 else 0) + (curr2.data if curr2 else 0)

            carry = (1 if sum >= 10 else 0)
            sum = sum % 10
            temp = Node(sum)
            if res is None:
                res = temp

            else:
                prev.next = temp

        if carry > 0:
            temp.next = Node(carry)

        ans = self.reverse(res)
        return ans
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
            






    def pop(self,position=None):# 0 index bugged.

        if not position: position = len(self)-1
 
        index = 0
        if self.head is None:
            return
        if position is None:
            while (self.head.next != None):
                self.head = self.head.next
            self.head = None
        
        current = self.head
        while current.next and index <= position:
            previous = current
            current = current.next
            index += 1
            
        if index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next    
        print(f' The popped node is {current}')

                
            
        
    def sort(self):
        sorted = None
        current = self.head
        while (current != None):
            next = current.next
            sorted = sorted(sorted,current)
            current = next
        self.head = sorted
        return self.head

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

    def insert(self,position,data):#no work
        head = self.head
        if(position < 1):
            newNode = Node(data)
            newNode.next = self.head
            head = newNode
        else:
            while (position != 0):
                position -= 1

                if (position == 1):
                    newNode = data
                    newNode = head.next
                    head.next = newNode
                    break
                head = head.next
                if head == None:
                    break
            if position != 1:
                print('position out of range')
        return head
        


        
                
        
        
        
            

            
        
        
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

    
 
    x.append(6)
    y.append(6)
    x.append(2)
    y.append(2)
    x.append(3)
    y.append(3)
    print(x,y)
    x.insert(2,69)
    y.insert(2,69)
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













    # x.pop()
    # y.pop()
    # print(x,y)
    # x.append(x)   x.copy(z)     x.extend(x)    x.insert(x)    x.remove(x)  
    # x.sort(x)  x.clear(x)    x.count(     x.index(x)     x.pop(x) 
    # x.reverse(x)

    # as a function
    # linked list
