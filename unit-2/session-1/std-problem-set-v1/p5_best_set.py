'''
U:
i/p = id: artist [dict]
o/p = str

#edge cases
1. empty
2. tie > return either

P:
count_dict [artist] = 
max = 
'''

def best_set(votes):
    count_dict = {}
    
    for vote in votes:
        artist = votes[vote]
        if artist in count_dict:
            count_dict[artist] += 1
        else:
            count_dict[artist] = 1
    #return count_dict
    max_count = max(count_dict.values())
    for artist in count_dict:
        if count_dict[artist] == max_count:
            return artist


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))