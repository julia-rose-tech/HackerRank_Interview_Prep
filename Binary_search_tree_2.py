import sys
from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        if root is None:
            return
        
        # Create a queue for level-order traversal
        queue = deque()
        queue.append(root)  # Start with the root node
        
        while queue:
            current_node = queue.popleft()
            print(current_node.data, end=' ')  # Print the data of the current node
            
            # Enqueue left child if it exists
            if current_node.left:
                queue.append(current_node.left)
            
            # Enqueue right child if it exists
            if current_node.right:
                queue.append(current_node.right)
        
   
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
