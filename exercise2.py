# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    
    foods = ('berries', 'vegetables', 'legumes')

    meal = ''

    for food in foods:
        
        meal += food + ', '

    return meal
    
# Call the function and print the result
print('Exercise 2:', combine_foods()) 

