# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food...
# ...strings in the foods to a variable named last_two_foods.

def slice_foods():

    foods = ('berries', 'vegetables', 'legumes')

    last_two_foods = foods[-2:]

    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())
