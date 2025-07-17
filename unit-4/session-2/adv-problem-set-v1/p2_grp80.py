"""
UPI Method
Understand: Find the keywords with maximum frequency
For eg: action -> 3 times (scene 1, scene 2, and scene 4)
        hero -> 3 times (scene 1, scene 2, scene 3)


Plan: 
Edge cases: empty cases (ignore)

Happy cases:
Most of the input we assume are gonna be happy cases

Implementation: 


Solution:
Space Complexity: scenes: x
                  keywords: k
                  y < k * x
                  y <= k * x
Time Complexity: is it O(n) or O(n^2)
    O(nk) loop through n then all keywords(nk)
    O(< k*x) kx is the num of all keywords, but there are 2 loop
"""

def find_most_frequent_keywords(scenes):
    #T = O(nk), M = O(n)
    word_count = {}
    for keywords in scenes.values():
        for keyword in keywords:
            if keyword in word_count:
                word_count[keyword] += 1
            else:
                word_count[keyword] = 1
    max_freq = max(word_count.values())
    res = []
    for word in word_count:
        if word_count[word] == max_freq:
            res.append(word)
    return res




scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) 