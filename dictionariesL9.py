# /users/tannerwilliams/desktop/ME 499/ME499_ClassExamples

""" Dictionaries Overview
    - Group unique (key, value) pairs
        - keys: can be any type
        - values: can be any type
    - Unordered
    - Different applications than lists
    - **kwargs
    - AKA 'hashmaps', 'tables', etc. in other languages
    - Ordered dictionaries are different than regular (unordered)
    - Common uses:
        - Storing data
        - lent
    - Cannot append to dictionaries
    - Multiple extensible functions
"""


""" Creating a dictionary
    - {} or dict()
    - {"Object":"Car, "Type":"Dodge", "year":2017}
"""
some_list = [(1, 2), (3, 4)]
some_dictionary = dict(some_list)
print(some_dictionary)


""" Concatenating Dictionaries
    - CANNOT use a + sign
    - 
"""
some_dict = {'Object':'Car', 'Type':'Dodge', 'Year':2017}


""" Dictionary Methods 
    - clear() [removes all elements from the dictionary]
    - copy() [returns a copy of the specified dictionary]
    - fromkeys() [returns a dictionary with specified key and value]
    - get() [returns the value of specified key]
    - 
"""


""" Dictionary Looping 
    - Go through a dictionary and locate/view respective object for key, etc. 
"""
print(" Dictionary looping")
for key in some_dict:
    value = some_dict[key]
    print(key, value)
