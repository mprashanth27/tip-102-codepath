'''
U-nderstand: check if a pallindrome
i/p = post titles : str
o/p = boolean

#Constraints: ignore spaces, punctuation, and case

#Edge cases
1. "" > True
2. Alpha numeric ~ "a1c c1a" > True?
3. odd #chars ~ "ab a ba" > True

P-lan:
p-1:
s.lower()
s.strip(" ") # wont work as it only remove spaces at ends not from middle
use 2 ptr's l,r while skipping punctuation's to check if char is same if not return false

I-mplement:
'''
def is_symmetrical_title(title):
    title = title.lower()
    # initialze 2 ptrs
    l, r = 0, len(title) - 1

    while l <= r:
        # check if current char's pointed by l & r are alphanumeric, if not update ptr's
        while not title[l].isalnum():
            l += 1
        while not title[r].isalnum():
            r -= 1
        
        # check if l & r val's are same, if yes continue
        if title[l] == title[r]:
            l += 1
            r -= 1
        else:
            return False
    
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))

print(is_symmetrical_title("a1c c1a"))
print(is_symmetrical_title("ab a ba"))