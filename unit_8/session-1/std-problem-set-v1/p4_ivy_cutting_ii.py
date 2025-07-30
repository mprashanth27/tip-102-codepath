'''
You have a trailing ivy plant represented by a binary tree. 
    You want to take a cutting to start a new plant using the rightmost vine in the plant. 
        Given the root of the plant, return a list with the value of each node in the path from the root node to the 
            rightmost leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale 
    for why you believe your solution has the stated time complexity. Assume the input tree is balanced when 
        calculating time complexity.

Understand:
Input: root
Output: list that stores the value of every rightmost node from that root

Plan:
1. Create an array that stores the value
2. append value of root into that array
3. current = root
4. while current:
    arr.append(current.right.val)
    current=current.right
5. Return the array
'''
from tree_node import TreeNode

# def right_vine(root):
#     rightNodes = []
#     current = root
#     while current:
#        rightNodes.append(current.val) 
#        current = current.right
    
#     return rightNodes

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))


'''
*
 \
  * 
   \ 
    * 
      \

Plan:
init solution
1. base: 
    if not node:
        return
2. - append the node.val to the solution array in-place
   - go to the right i.e. call the function on node.right

- Call the helper function on root.right
'''

def traverse(node, path):
        
    if not node:
        return path
        
    path.append(node.val)
    traverse(node.right, path)
    
def right_vine(root):
    traversal = []  
    traverse(root, traversal)
    return traversal

print(right_vine(ivy1))
print(right_vine(ivy2))