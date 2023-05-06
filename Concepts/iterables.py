""""
In this python file, I'll try and learn about iterable objects using the Python languages

"""

# The map function is basially equivalent to a python list comprehension
# map(f, iterable) ~= [f(x) for x in iterable]

# List comprehension: [ start : end : step]
example = [1, 2, 3, 4, 5]
print(f"Original list: {example}")
# Reversal
print(f"Reversal: {example[::-1]}")
# Peek at top (last item in list)
print(f"Last element: {example[-1:]}")