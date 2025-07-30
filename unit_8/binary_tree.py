"""
Note: Testing your Binary Tree (Printing)
To keep the amount of starter code manageable, we have chosen not to include a function to print a binary tree 
as part of each relevant problem statement. You may instead call the function print_tree() 
and use it as needed while you complete the problem sets.

Print Binary Tree Function
Accepts the root of a binary tree and prints out the values of each node level by level from left to right. 
Values of None are used to indicate a null child node between non-null children on the same level. 
Prints "Empty" for an empty tree.

# import for using TreeNode class and print_tree function
from binary_tree import TreeNode, print_tree

"""
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