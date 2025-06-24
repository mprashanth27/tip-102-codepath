'''
U-nderstand:

i/p = engagement rates: list[int]; sorted in non-decreasing order
o/p = list[int]; an array of the squares of each number sorted in non-decreasing order

#Constraints: Modify the solution below to use the two-pointer technique

#Edge cases
[]
only +ve; W/ & W/O duplicate values
0 & +ve; W/ & W/O duplicate values
-ve & 0; W/ & W/O duplicate values
[3,3,3,3,3]

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
#My two-pointer code
# NOTE:THIS CODE WAS WRITTEN ASSUMING THERE WILL BE -VE NUMS IN THE I/P LIST
# NEED TO VERIFY IF IT WORKS IF THEY ARE ONLY +VE NUMS IN THE I/P LIST

def engagement_boost(engagements):
    squared_engagements = [] # output arr
    
    def square_and_add_engagement(engagement_index): #helper func
        squared_engagement = engagements[engagement_index] * engagements[engagement_index]
        squared_engagements.append(squared_engagement)
    
  
    if engagements[0] < 0:
        # iterate thru i/p arr to find pivot i.e., 0 or 1st +ve num.
        for i in range(len(engagements)):
            if engagements[i] >= 0:
                pivot = i
                break
        
        list1_ptr = pivot # to move left from pivot
        list2_ptr = pivot + 1 # to move right from pivot
        while list1_ptr >= 0 and list2_ptr < len(engagements):
            if abs(engagements[list1_ptr]) < abs(engagements[list2_ptr]): # CHECK LATER! <=? i.e., what if engagements[list1_ptr] == engagements[list1_ptr]? 
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