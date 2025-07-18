'''
U-nderstand:

i/p = transmissions: list[int]
o/p = (,)

#Constraints: must have O(log n) time complexity.

#Edge cases
([], 0)


P-lan:
bfs()
helper()
    if mid != target:
    


I-mplement:
'''

def find_frequency_positions(transmissions, target_code):
    def binary_search(arr,target):
        l , r = 0, len(arr) - 1 
        
        while l < r:
            mid = (l+r)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    return binary_search(transmissions, target_code)



print(find_frequency_positions([5,7,8,8,8,8,8,8,8,8,8,10], 8))
# print(find_frequency_positions([5,7,7,8,10], 8))

#print(find_frequency_positions([5,7,7,8,8,10], 8))
# print(find_frequency_positions([5,7,7,8,8,10], 6))
# print(find_frequency_positions([], 0))