'''
U-nderstand:
i/p = race_times: list[int], threshold: int
o/p = int

Edge cases:
[] 
[0]
[-1,2]

P-lan:
count += for val in race_times if val < threshold

I-mplement:
'''
def count_less_than(race_times, threshold):
    res = 0
    for time in race_times:
        if time < threshold:
            res += 1
    return res    

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))