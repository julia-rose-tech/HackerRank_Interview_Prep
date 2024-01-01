class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1

# Function to print the tree in-order
def PrintTree(node):
    if node:
        PrintTree(node.left)
        print(node.data, end=' ')
        PrintTree(node.right)

T = int(input("Enter the number of nodes: "))
myTree = Solution()
root = None
for i in range(T):
    data = int(input("Enter node value: "))
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print("Height of the tree:", height)
print("In-order traversal of the tree:")
print(PrintTree(root))
