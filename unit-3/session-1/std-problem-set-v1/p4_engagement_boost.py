'''
U-nderstand:

i/p = engagement rates: list[int]; sorted in non-decreasing order
o/p = list[int]; an array of the squares of each number sorted in non-decreasing order

#Constraints: Modify the solution below to use the two-pointer technique

#Edge cases
1. []
2. only +ve; W/ & W/O duplicate values [1,2,3,4,5], [1,2,3,3,4,5] > Pass
3. only -ve; W/ & W/O duplicate values > Pass 
4. 0 & +ve; W/ & W/O duplicate values [0,1,2,3,4,5] > Pass
5. -ve & 0; W/ & W/O duplicate values [-3,-2,-1,0] > Pass
6. [3,3,3,3,3] > Pass

P-lan:
p1 : break list in to 2 halfs by length [WON'T WORK! as we would still need to sort it] 
eg: [-4, -1, 0, 3, 10]
[-4, -1, 0, 3, 10] > [-4, -1, 0] [ 3, 10]
squared: l1 = [16, 1, 0], l2 = [ 9, 100]                                                                                                                                                                                                                        
now use 2 same direction ptrs to merge them - l1 ptr, l2 ptr
l1[0]<l2[0]
res.append(l1[0]) 
else res.append(l2[0]) which would append [9] but there is 0 in l1 which will be out of place until you sort it.
So, need to break list in to halfs at 0 or 1st +ve num.

p2 : break list in to halfs at 0 or 1st +ve num.



I-mplement:
'''
#My two-pointer code: T = O(n), M = O(n)
def engagement_boost(engagements):
    if not engagements: # empty list 
        return []
    
    squared_engagements = [] # output arr
    
    def square_and_add_engagement(engagement_index): # helper func
        squared_engagement = engagements[engagement_index] * engagements[engagement_index]
        squared_engagements.append(squared_engagement)
    
    # engagements only has - ve numbers (square in reverse order for non-decreasing)
    if engagements[-1] < 0: 
        for x in range(len(engagements) - 1, -1, -1):
            square_and_add_engagement(x)
    # engagements only has + ve numbers
    elif engagements[0] >= 0:
        for j in range(len(engagements)):
            square_and_add_engagement(j)
    else: 
        # iterate thru i/p arr to find pivot i.e., 0 or 1st +ve num.
        for i in range(len(engagements)):
            if engagements[i] >= 0:
                pivot = i
                break
        
        list1_ptr = pivot # to move left from pivot
        list2_ptr = pivot + 1 # to move right from pivot
        while list1_ptr >= 0 and list2_ptr < len(engagements):
            if abs(engagements[list1_ptr]) < abs(engagements[list2_ptr]): # what if engagements[list1_ptr] == engagements[list1_ptr]? will append the square of the right pointer’s value (since <= is not used, but it still works for sorting since order is preserved by the merge).
                square_and_add_engagement(list1_ptr)
                list1_ptr -= 1
            else:
                square_and_add_engagement(list2_ptr)
                list2_ptr += 1

        while list1_ptr >= 0: # add if any nums remaining in list1
            square_and_add_engagement(list1_ptr)
            list1_ptr -= 1
        while list2_ptr < len(engagements): # add if any nums remaining in list2
            square_and_add_engagement(list2_ptr)
            list2_ptr += 1
    
    return squared_engagements

print(engagement_boost([-4, -1, 0, 3, 10])) # o/p = [0, 1, 9, 16, 100] Pass
print(engagement_boost([-7, -3, 2, 3, 11])) # o/p = [4, 9, 9, 49, 121] Pass
print(engagement_boost([1,2,3,4,5])) # o/p = [1, 4, 9, 16, 25] Pass
print(engagement_boost([1,2,3,3,4,5])) # o/p = [1, 4, 9, 9, 16, 25] Pass
print(engagement_boost([0,1,2,3,4,5])) # o/p = [0, 1, 4, 9, 16, 25] Pass
print(engagement_boost([0,1,2,3,3,4,5])) # o/p = [0, 1, 4, 9, 9, 16, 25] Pass
print(engagement_boost([-3,-2,-1,0])) # o/p = [0, 1, 4, 9] Pass
print(engagement_boost([3,3,3])) # o/p = [9, 9, 9] Pass
print(engagement_boost([-3,-2,-1])) # o/p = [1, 4, 9] Pass
print(engagement_boost([-1])) # o/p = [1] Pass
print(engagement_boost([0])) # o/p = [0] Pass
print(engagement_boost([1])) # o/p = [1] Pass
print(engagement_boost([])) # o/p = [] Pass