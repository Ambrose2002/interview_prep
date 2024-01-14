
class Node:
    
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        

class LinkedList:
    
    def __init__(self, head = None):
        self.head = head
        
    def createLL(self, lst, n):
        root = Node(lst[0])
        temp = root
        for i in range(1, n):
            temp.next = Node(lst[i])
            temp = temp.next
        return root
    
    
lst = [1,2,3,4,5,6]
n = len(lst)
root = LinkedList().createLL(lst, n)
print(root.val)
        