'''
U-nderstand:
i/p = comments : list[str]
o/p = comments in reverse: list[str]

#Edge cases
1. No comments ~ []
2. Duplicates ~ ["Great post!", "Love it!", "Great post!"]

Reverse the order using a stack!
P-lan:
1. add all comments to stack 
2. res.append(stack.pop())

I-mplement:
'''
def reverse_comments_queue(comments):
    # T = O(n), M = O(n)
    stack = [] # ~ M = O(n)
    res = [] # ~ M = O(n)

    #Build stack
    for comment in comments: # ~ T' = O(n)
        stack.append(comment)
  
    while stack: # ~ T' = O(n)
        res.append(stack.pop())

    return res

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))