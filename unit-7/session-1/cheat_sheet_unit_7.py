def count_recursive(num):
    i = 1
    print(f"Count {i}!")
    if num == i:
        return
    else:
       count_recursive(i + 1)

count_recursive(5)

'''Recursive Driver and Helper Functions'''
def partition_evens_odds(lst): # driver function
  return recurse_partition(lst, [], [])

def recurse_partition(lst, evens, odds): # helper function
  if not lst:
      return evens, odds
  if lst[0] % 2 == 0:
      evens.append(lst[0])
  else:
      odds.append(lst[0])
  return recurse_partition(lst[1:], evens, odds)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = partition_evens_odds(lst)
print(evens) # Prints: [2, 4, 6, 8]
print(odds)  # Prints: [1, 3, 5, 7, 9]
''' '''


