'''
U-nderstand:
i/p = list<int>
o/p = list<int>

Edge cases:
[] 
[0]
[-1,2]

P-lan:
res = [val * 2 for val in i/p list]
'''
# I-mplement:
def doubled(hunny_jars):
    return [val * 2 for val in hunny_jars]

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

hunny_jars = []
print(doubled(hunny_jars))