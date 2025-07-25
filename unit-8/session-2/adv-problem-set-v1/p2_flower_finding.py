'''
U-nderstand:
Assume the input tree is balanced when calculating time and space complexity.

i/p =  root of the binary search tree inventory, a target flower name
o/p = boolean

#Constraints:

#Edge cases
[] #empty
["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"] # non-bst

M-atch:

P-lan:
binary search 

if not collection:
            return None
    result = []
    def binary search(node):
        if node: 
            inorder(node.left)
            result.append((node.key, node.val))
            inorder(node.right)
        
        
    inorder(collection)
    return result

I-mplement:

R-eview:

E-valuate:
'''
from binary_tree import TreeNode,print_tree
from collections import deque 

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def find_flower(inventory, name):
    pass

"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 