"""
UPI
U-nderstand:
We need to find the number of unique characters (keys) in the hashmap/dict
i/p = dict{chrac:dialogue}
o/p = 

#Constraints: 

#Edge cases


P-lan:


I-mplement:

"""

def count_unique_characters(script):
  return len(script)

script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 