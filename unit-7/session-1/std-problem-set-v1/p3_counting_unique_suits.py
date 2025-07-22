'''
U-nderstand: count the total number of unique suits in the list.

i/p = stones: list[int]
o/p =  int

#Constraints:

#Edge cases
1. empty ~ [] > 0 
3. 1 element ~ ["Mark I"] > 1 
2. duplicates ["Mark I", , "Mark I"] > 1 

Match: set

P-lan:
# count_suits_iterative
p-1 : if suit not in seen set, inc count


I-mplement:
'''
def count_suits_iterative(suits):
    # T = O(n), M = O(n) 
    seen = set() # ~ M = O(n) 
    unique_suits_count = 0

    for suit in suits: # ~ T = O(n)
        if suit not in seen:
            seen.add(suit)
            unique_suits_count += 1
    
    return unique_suits_count


def count_suits_recursive(suits):
    pass

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
#print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
