'''
U-nderstand: 
i/p = list<int>
o/p = int 

Edge cases:
[] 
[0]
[-1,2]
'''

def sum_honey(hunny_jars):
    if not hunny_jars: # empty list
        return 0
    
    total = 0
    for val in hunny_jars:
        total += val
    return total

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))