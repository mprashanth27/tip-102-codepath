'''
U-nderstand: check if nums could become non-decreasing ~ increasing by modifying at most one element.
modify means delete or swap or both?

i/p = nums: list[int]
o/p = Boolean

#Constraints: can modify at most one element

#Edge cases
[] > T # empty
[1] > T # 1 element
[1,4,3]? > T
[1,2,2,3]? > T
[1,2,-4] > T
[-1,-2,-3] > F

P-lan:
p2 - .sort & count #diff's
p3 - sort using 2 ptrs [l,r] & count #swaps


I-mplement:
'''
# need to revisit this and verify if this logic is perfect
def non_decreasing(nums):
    if len(nums) < 2: # empty or 1 element
        return True

    ptr1, ptr2 = 0 , 1
    pop_count = 0
    while ptr1 < len(nums) and ptr2 < len(nums):
        if nums[ptr1] <= nums[ptr2]:
            ptr1 += 1
            ptr2 += 1
        elif nums[ptr1] > nums[ptr2] and pop_count < 1:
            nums.pop(ptr1)
            pop_count += 1
        else:
            return False
    return True

# actual outputs for below Edge cases were same as expected [All Pass]
# nums = [4, 2, 3]
# print(non_decreasing(nums))

# nums = [4, 2, 1]
# print(non_decreasing(nums))

# nums = [1,4,3]
# print(non_decreasing(nums))

# nums = [3, 4, 2, 3]
# print(non_decreasing(nums))

nums = []
print(non_decreasing(nums))

nums = [1]
print(non_decreasing(nums))

nums = [1,2,2,3]
print(non_decreasing(nums))

nums = [1,2,-4]
print(non_decreasing(nums))

nums = [-1,-2,-3]
print(non_decreasing(nums))
