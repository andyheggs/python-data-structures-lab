# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the ...
# ...home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

home_town = {

    'city': 'Sulby',
    'state': 'Isle of Man',
    'population': 85000,

}

def list_home_town_items():

    # with list comprehension and view objects:
        # list comp to iterate over each KVP (f{key}={val})
        # format home-town items as <key> = <value> string for each K:V pair in dict.        
        #return list of KVP as tuples using view object 'home_town.items()' to iterate over list
        
    home_town_items = [f'{key} = {value}' for key, value in home_town.items()]

    return home_town_items        


# Call the function and print the result
print('Exercise 5:', list_home_town_items())
