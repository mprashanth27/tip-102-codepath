'''
U-nderstand:

i/p = engagement rates: list[int]; sorted in non-decreasing order
o/p = list[int]; an array of the squares of each number sorted in non-decreasing order

#Constraints:

#Edge cases


P-lan:


I-mplement:
'''
#CodePath initial code
def engagement_boost(engagements):
    squared_engagements = [] # output arr
    
    # iterate thru i/p arr, square them & add to o/p arr
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True) # sort output arr in ascending order
    #print(squared_engagements) #[(100, 4), (16, 0), (9, 3), (1, 1), (0, 2)]
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
#print(engagement_boost([-7, -3, 2, 3, 11]))