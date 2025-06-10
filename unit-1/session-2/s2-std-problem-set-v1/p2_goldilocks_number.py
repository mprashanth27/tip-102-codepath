'''
U-nderstand:
i/p = nums : list[int]
o/p = num: int

Edge cases:
[3,3,4,4]
[]

P-lan:
max,min
return num != max & min

I-mplement:
'''
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    
    min_val = min(nums)
    max_val = max(nums)
    
    for num in nums:
        if num != min_val and num != max_val:
            return num
    
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))