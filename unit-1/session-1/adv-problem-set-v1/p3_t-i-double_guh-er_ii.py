'''
U-nderstand:
returns a new string that removes any substrings t, i, gg, and er from word. 

i/p = word: str
o/p = new string

#Constraints: The function should be case insensitive.

#Edge cases
""
mix of single chars of double chara substrings eg. "Triggger" > rg PASS
"cat dog" # spaces b/w words? ASSUME NO


P-lan:
if not empty
word.lower()
iterate using while w/ index
if in "t", "i" skip word[i] and inc i+1
elif word[i:i+2] in "gg", "er" skip word[i:i+2] and inc i+2
else:
res.app(chara)


I-mplement:
'''
# T = O(n), M = O(n)
def tiggerfy(word):
    if not word:
        return ""
    
    word = word.lower()
    chara_to_remove = {"t", "i"}
    double_characs_to_remove = {"gg", "er"}
    res = [] # ~ M = O(n)
    
    i = 0
    while i < len(word):
        if word[i] in chara_to_remove:
            i += 1
        elif word[i : i+2] in double_characs_to_remove:
            i += 2
        else:
            res.append(word[i]) # ~ T = O(1) 
            i += 1
    return ''.join(res) # ~ T = O(n) 

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

word = "Triggger"
print(tiggerfy(word))