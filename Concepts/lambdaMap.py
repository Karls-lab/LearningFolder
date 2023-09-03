"""
The lambda function is defined as: lambda arguments : return expression
In simple terms, they are 'one-use' functions without names
"""

print((lambda x: x + 3)(3))

list1 = [x for x in range(1, 11)]
even = list(map(lambda x: True if x % 2 == 0 else False, list1))
even_dict = dict(zip(list1, even))
print(even_dict)


"""The map function is a python built in that applies a function to each item in an iterable
    The map function returns a map object which can be converted to other iterable types such as lists"""
# General syntax: map(function, iterable)
# Example 01: doubling numbers:
numbers = [1,2,3,4,5,6]
doubled = map(lambda x: x * 2, numbers)
result = list(doubled)
print(result)

# Example 02: Converting Strings to uppercase:
names = ['bob', 'frank', 'alice']
uppercase_names = list(map(str.upper, names))
print(uppercase_names)

# Example 03: Length of strings:
names = ['cain', 'robert', 'courtney', 'karl']
lengths = list(map(len, names))
print(lengths)