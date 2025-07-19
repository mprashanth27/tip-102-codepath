'''
U-nderstand:

i/p = stones: list[int]
o/p = sum(stones): int

#Constraints: using a recursive approach

#Edge cases
[] > 0 #Pass
[0] > 0 #Pass
[1] > 1 #Pass

P-lan:
#p1 [modifies i/p list]
if stones not empty> return stones.pop() + sum_stones(stones)

#p2 [w/o modifiying i/p list]

I-mplement:
'''
# T = O(n), M = O(n) ~ due to recursion depth
def sum_stones(stones):
    def sum_helper(index = 0):
        if index == len(stones): # base case
            return 0
        return stones[index] + sum_helper(index + 1) # no need to send stones during recursive calls as it is not being modified 
    return sum_helper()
    

print(sum_stones([5, 10, 15, 20, 25, 30])) # = 105 #Pass
print(sum_stones([12, 8, 22, 16, 10])) # = 68 #Pass

print(sum_stones([]))
print(sum_stones([0]))
print(sum_stones([1]))
