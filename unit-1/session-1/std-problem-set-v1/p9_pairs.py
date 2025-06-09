'''
U-nderstand:
i/p = item_quantities: list[int]
o/p = Boolean

Edge cases:
[]
[-1,2]?

P-lan:
for loop
if qty odd> false

I-mplement:
'''
def can_pair(item_quantities):
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))