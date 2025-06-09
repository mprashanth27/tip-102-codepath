'''
U-nderstand:
i/p = s: str
o/p = s: str

Edge cases:
""
1?
"1at"
"Hat"

P-lan:
iterate & add to o/p str if letter not t, i, g, e, and r

I-mplement:
'''
def tiggerfy(s):
    res = ""
    for c in s:
        c_lowered = c.lower()
        if c_lowered != "t" and c_lowered != "i" and c_lowered != "g" and c_lowered != "e" and c_lowered != "r":
            res += c
    return res

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))