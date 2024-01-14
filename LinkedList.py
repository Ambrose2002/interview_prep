class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev
        
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def countNodes(self):
        i = 0
        if self.head is None:
            print('LinkedList is empty')
        
        else:
            current = self.head
            while current is not None:
                current = current.next 
                print(type(current))
                i += 1
                
        print('LinkedList has {} nodes'.format(i))
            
    
        
    def pushstart(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node
        
    def pushend(self, new):
        new_node = Node(new)
        if self.head == None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node
        
    
    
    def pushafter(self, new, pos):
        new_node = Node(new)
        if pos < 1:
            print('Invalid position input')
            
        elif pos == 1:
            new_node.next = self.head
            self.head = new_node
            
        else:
            temp = self.head
            for i in range (1, pos-1):
                if temp is not None:
                    temp = temp.next 
                    
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
                
            else:
                print('Position is out of range')
                    
        
        
    def removeend(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None 
            return
        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next
        second_last.next = None
        return
                
    def removehead(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None 
        else:
            self.head = self.head.next
            
    def removeafter(self, pos):
        if pos < 1:
            print('Invalid postion input')
            
        elif pos == 1:
            self.head = self.head.next 
            
        else:
            temp = self.head
            for i in range (1, pos-1):
                if temp is not None:
                    temp = temp.next
                
            if temp is not None:
                if temp.next is not None:
                    temp.next = temp.next.next
                # print('Position is out of range')
            else:
                print('Postion is out of range')
                
        
    def printlist(self):
        linkedlist = []
        current = self.head
        if current is None:
            print('List is empty')
            
        else:
            while current is not None:
                linkedlist.append(current.val)
                current = current.next
        print(linkedlist)
                
# a = Node('A')
# b = Node('B')
# c = Node('C')

# a.next = b
# b.next = c

ll = LinkedList()
ll.pushstart(3)
ll.pushstart(4)
ll.pushstart(10)
ll.pushend(20)
# ll.removeend()
# ll.removehead()
ll.pushafter(200, 3)
ll.removeafter(3)
ll.pushafter(20, 2)
ll.countNodes()
ll.printlist()
        