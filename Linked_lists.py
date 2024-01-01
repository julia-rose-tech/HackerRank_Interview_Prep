# Sample Input:
# 4
# 2
# 1
# 3
# 4

# Sample OutPut:
# 2 1 3 4

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    
    # inserts each data element to end of the list
    def insert(self, head, data):
        new_node = Node(data)
        if not head:
            head = new_node
        else:
            current = head #temporary pointer points to head
            while current.next: #loop until current.next becomes 'None'
                current = current.next #inside loop, the pointer is being moved to the next
            current.next = new_node #current.next now equals none, so the new_node is added here at the end of the list
        return (head) 


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  