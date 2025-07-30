from tree_node import TreeNode

'''
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! 
    Given the root of a binary tree representing your oak tree, count the number of leaf nodes in the tree. 
        A leaf node is a node that does not have any children.

Understand:
Input: Tree, root of tree
Output: number of treenodes in that tree. integer

Match: binary tree

Plan:
1. int total
2. Base case
    # if node is none -> 
        return 1
   Recursively
   # total + call the function on left
   # total + Call the function on right
'''

def count_leaves(root):

    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    leftleaves = count_leaves(root.left)
    rightleaves = count_leaves(root.right)

    return leftleaves+rightleaves
    

   


"""
Nice!!!!!

total = 0
def helper(node):
    if not node:
        return 
    
    if not node.left and not node.right:
        total += 1
    
    helper(node.left)
    helper(node.right)
    
helper(root)
r
    
    
    helper(node.right)
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))