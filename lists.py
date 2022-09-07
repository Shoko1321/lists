

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

    def __getitem__(self, index):

        counter = 0
        current = self.head
        while current != None:
            if index == counter:
                return current.data
            counter +=1  
            current = current.next

        raise IndexError

    def __len__(self):
        counter = 0
        current = self.head
        while current != None:
            current = current.next
            counter += 1
        return counter
        
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
            
  
        
    def __str__(self):
        ret = '<'
        cur = self.head
        while cur != None:
            ret += str(cur.data)
            cur = cur.next
            ret += ','
        return ret[:-1] + '>'
    __repr__ = __str__




    def pop(self,position=None):

        if not position: position = len(self)-1
 
        index = 0
        if self.head is None:
            return
        if position is None:
            while (self.head.next != None):
                self.head = self.head.next
            self.head = None
        
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
            
        if index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next       
        print(current)
    
    # def pop_back(self):
    #     if(self.head != None):
    #         if(self.head.next == None):
    #             self.head = None
    #         else:
    #             temp = self.head
    #             while(temp.next.next != None):
    #                 temp = temp.next
    #             last_Node = temp.next
    #             temp.next = None
    #             print(last_Node)
    #             last_Node = None
                
            
        
    def sort(self):
        sorted = None
        current = self.head
        while (current != None):
            next = current.next
            sorted = sorted(sorted,current)
            current = next
        self.head = sorted
        return self.head

    def index(self,value):
        current = self.head
        count = 0

        while (current):
            if(current.data == value):
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
        while(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None

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
    def insert(self, prev_node, data):
        if prev_node is None:
            print ("does not compute")
            return
        new_node = Node(data = data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        
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

    x.append(2)
    y.append(2)
    x.append(3)
    y.append(3)
    x.append(4)
    y.append(4)
    print(x,y)
    x.insert(2,69)
    y.insert(2,69)
    print(x,y)
    # x.remove(2)
    # y.remove(2)
    # print(x,y)

    # x.append(3)
    # y.append(3)
    # print(x,y)
    # x.append(3)
    # y.append(3)
    # z = x[425]
    # print(z)
    # print(x,y)
    # x.append(1)
    # y.append(1)
    # # print(x,y)
    # x.pop(1)
    # y.pop(1)
    # print(x,y)
    # x.reverse()
    # y.reverse()
    # print(x,y)
    # x.sort()
    # y.sort()
    # try:
    #     print(x.index(2))
    # except ValueError:
    #     print("2 is not in xa")

    # try:
        
    #     print(y.index(5))

    # except ValueError:
    #     print("5 is no index")
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
