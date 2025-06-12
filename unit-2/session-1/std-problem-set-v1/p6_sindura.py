#U:
#input: array of number of audience
#output: combined audience size if that size is the max size

#edge cases:
#empty array
# if only one max

#plan:
# max of audiences
# loop: each audience in audiences
# if audience is equal to max
# return the sum of the audience

def max_audience_performances(audiences):
    max_audience = max(audiences)

    for audience in audiences:
        if audience == max_audience:
            return sum(audience)

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))