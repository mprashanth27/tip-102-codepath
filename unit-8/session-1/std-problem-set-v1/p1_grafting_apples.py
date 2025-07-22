'''
You are grafting different varieties of 
    apple onto the same root tree can produce many 
        different varieties of apples! Given the following TreeNode class, create the binary tree depicted below.
            The text representing each node should should be used as the value.
                The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

Understand: Input root, output: nothing is returned create the tree
Match: binary tree
Plan: Create each node and assign lefts and rights

'''
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

root = TreeNode("Trunk")
node1 = TreeNode("Macintosh")
node2 = TreeNode("Granny Smith")
node3 = TreeNode("Fuji")
node4 = TreeNode("Opal")
node5 = TreeNode("Crab")
node6 = TreeNode("Gala")

root.left=node1
root.right=node2
node1.left=node3
node1.right=node4
node2.left=node5
node2.right=node6

print_tree(root)