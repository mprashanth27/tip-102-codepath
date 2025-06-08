'''
Understand: 
i/p = list, a non-negative integer x
o/p = list[i]

Edge cases:
[] 
x = -1
'''

def get_item(items, x):
    if x >= 0 and x < len(items) and items:
	    return items[x]
    return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))