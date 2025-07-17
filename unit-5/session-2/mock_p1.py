''''
Q. https://leetcode.com/problems/palindrome-linked-list/description/
Understand: palindrome LL

i/p: 1>2>3>2>1
o/p: Boolean

#constraints:


plan:
Edge cases:
1. 1>2>3>2>1 = T
2. 1>2>3>3>2>1 = T
3. [] = T
4. 1>2>4>3>2>1 

psuesdocode:

1. itearate LL to get #nodes ~ tail
2. set left ptr as head , right ptr tail
3. while l < r:
    3a. if ll[l] = ll[r]
        conitnue
    return false

'''
class node:
    def __init__(self, data, next, prev):
        self.data = 0
        self.next = None
        self.prev = None

    def palindrome(self, head):
        head = head
        cur = head
        while cur.next:
            temp = node()
            temp.data = cur.data
            temp.next = cur.next
            temp.prev = cur


'''
'''