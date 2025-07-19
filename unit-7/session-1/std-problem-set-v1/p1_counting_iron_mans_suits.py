'''
U-nderstand: retrun #suits

i/p = suits: list[str]
o/p = count: int

#Constraints: 
1. Implement the solution iteratively without the use of the len() function

#Edge cases
[] > 0 #Pass
["Mark I"] > 1 #Pass


P-lan:
# iterative


I-mplement:
'''
# 1.Implement the solution iteratively without the use of the len() function.
def count_suits_iterative(suits):
    # T = O(n), M = O(1)
    count = 0
    while suits:
        suits.pop()
        count += 1
    return count

# 2.Implement the solution recursively.
def count_suits_recursive(suits):
    # T = O(n), M = O(n) ~ due to recursion depth
    recursive_count = 0
    def recursion(suits):
        nonlocal recursive_count

        if not suits: # base case
            return recursive_count
        
        suits.pop()
        recursive_count += 1
        return recursion(suits)
    return recursion(suits)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

print(count_suits_iterative([]))
print(count_suits_recursive([]))

print(count_suits_iterative(["Mark I"]))
print(count_suits_recursive(["Mark I"]))

# 3. Discuss: what are the similarities between the two solutions? What are the differences?
'''
main logic is same i.e., check suits is not empty > pop > increment the count.
inorder to iterate while is used in #1 and recursive calls in #2
'''