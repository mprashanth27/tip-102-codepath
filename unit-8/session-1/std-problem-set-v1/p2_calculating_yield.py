"""
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. 
Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
The root has a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe 
your solution has the stated time complexity.

Understand:
1. 3 nodes, root is a string with the operation, children are numbers
2. Ou2tput: result of the operation applied onto the children, integer

Match: Binary tree

Plan:
1.  if root.value == "+":
        return root.left+root.right
    elif root.value == "-"
        return root.left-root.right
    else:
        return root.left*root.right
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def calculate_yield(root):
  if root.val == "+":
      return root.left.val+root.right.val
  elif root.val == "-":
      return root.left.val-root.right.val
  else:
      return root.left.val*root.right.val
  
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))