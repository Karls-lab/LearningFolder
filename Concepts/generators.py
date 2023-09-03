"""
In this python program file, I'll show what a generator function is in python

A Python Generator is used to created your own iterable function
it returns an iterable object

"""

# The any() function returns true if any epxreession inside the iterable is true
# Generator expressions don't take up memory space. 

# For exapmle, these two expressions are the same, but the generator expression doesn't take up memory space
squares = sum([x*x for x in range(1, 11)])
squares = sum(x*x for x in range(1, 11))


# Example 2: 
companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}}

# One-Liner 
illegal = [x for x in companies if any(y<9 for y in companies[x].values())]
print(illegal)
