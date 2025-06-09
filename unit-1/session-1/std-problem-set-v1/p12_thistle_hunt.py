'''
U-nderstand:
i/p = items: list[str]
o/p = indices: list[int]

Edge cases:
[]
["book", "bouncy ball"] # No "thistle"

P-lan:
iterate & add index to o/p list if thistle

I-mplement:
'''
def locate_thistles(items):
    res = []
    for i,v in enumerate(items):
        if v == "thistle":
            res.append(i)
    return res

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))

items = []
print(locate_thistles(items))