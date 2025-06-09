'''
U-nderstand:
i/p = quantity: int
o/p = all divisors of quantity: list[int]

Edge cases:
0
-1
3 # odd

P-lan:

I-mplement:
'''
def split_haycorns(quantity):
    divisor = quantity
    res = []
    while (divisor > 0):
        if quantity % divisor == 0:
            res.append(divisor)
        divisor -= 1
    return res

quantity = 6
print(split_haycorns(quantity)) # [6, 3, 2, 1]
'''Note: if you want O/P to be [1, 2, 3, 6], initialize divisor = 1 & do while (divisor < quantity)'''

quantity = 1
print(split_haycorns(quantity))
