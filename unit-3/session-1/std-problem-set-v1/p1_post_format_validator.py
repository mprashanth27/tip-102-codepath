'''
U-nderstand:
i/p = : str - [] {} ()
o/p = : Boolean

# Edge cases: 
"(]" > False
"(" > False
"[(])" > False
"" ? 

P-lan:
add opening brackets to stack 
if u see a closing bracket, verify if it matches the closing & pop stack
  if yes, continue
  else return False

I-mplement:
'''

def is_valid_post_format(posts):
  stack = []
  opening_brackets = {"{", "[", "("}
  bracket_pairs = {"}":"{", "]":"[", ")":"("}
  for char in posts:
    if char in opening_brackets:
      stack.append(char)
    elif char in bracket_pairs:
      if not stack or stack[-1] != bracket_pairs[char]:
        return False
      stack.pop()

  return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
print(is_valid_post_format("")) # True
print(is_valid_post_format("]")) # False