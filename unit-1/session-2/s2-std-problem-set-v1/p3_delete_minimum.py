'''
U-nderstand:
i/p = hunny_jar_sizes: list[int]
o/p = jar_sizes_removed_order : list[int]

Edge cases:
[5, 2, 1, 8, 2]
[]

P-lan:
BF- sort(rev = True)
opt - 2 ptr?

#BF as per Qn req
sort(rev = True)
res.append(pop())

I-mplement:
'''
# T = O(nlogn), M = O(n)
def delete_minimum_elements(hunny_jar_sizes):
    if not hunny_jar_sizes:
        return []

    hunny_jar_sizes.sort(reverse = True) # T = O(nlogn)
    #print(hunny_jar_sizes)
    jar_sizes_removed_order = [] # M = O(n)
    while (hunny_jar_sizes):
        jar_sizes_removed_order.append(hunny_jar_sizes.pop())
    return jar_sizes_removed_order

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = []
print(delete_minimum_elements(hunny_jar_sizes)) 