"""
Q: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
U:

edge cases
[] [] both empty
[], l2 or 1 is empty
l1 & l2 don't intersect

P:
if both empty or  1 is empty > retrun  Null

cur1 = head1 & Cur2 =head2

while cur1 & cur2:
    if cur1 == cur2:
     return cur1
    cur1 = cur1.next
    cur2 = cur2.next
return Null

l1 & l2 don't intersect
"""