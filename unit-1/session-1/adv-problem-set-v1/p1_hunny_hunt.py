'''
U-nderstand:

i/p = items : list[str]
o/p = first index of target in items, and -1 if target is not in the lst

#Constraints: Do not use any built-in functions

#Edge cases
[] > -1
case sensitive?

P-lan:
assuming i/p, target are in same case.
1. iterate the list using range
    1a. check if current item == target
    1b. if yes, return index
2. target not found so return -1

I-mplement:
'''
# T = O(n), M = O(1)
def linear_search(lst, target):
	for i in range(len(lst)):
		if lst[i] == target: # assuming case insensitive
			return i
	return -1
			

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))