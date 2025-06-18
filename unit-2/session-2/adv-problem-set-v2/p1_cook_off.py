'''
U:
i/p = ingredients: str
o/p = #meals: int

#edge cases
1. empty
2. tie > return either

P:
count_dict [artist] = 
max = 
'''

def max_attempts(ingredients, target_meal):
    # Group 68 Soln
    ingredients_count = {}
    target_meal_count = {}

    for i in ingredients:
        if i in ingredients_count:
            ingredients_count[i] += 1
        else:
            ingredients_count[i] = 1

    for i in target_meal:
        if i in target_meal_count:
            target_meal_count[i] += 1
        else:
            target_meal_count[i] = 1

    counter = float('inf')
    
    for i in target_meal_count:
        #print("Curr Char is " + i)
        if ingredients_count[i] == 0:
            return 0
        #print("This is" + str(ingredients_count[i]))
        curr = ingredients_count[i]/target_meal_count[i]
        if (curr < counter):
            counter = curr
    return counter

# target_meal_count

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"

print(max_attempts(ingredients1, target_meal1))