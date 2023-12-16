"""
The Map Function is used to apply a function 
to every element in an iterable. 
"""

myList = [1, 2, 3, 4, 5]
myMap = list(map(lambda x: x**2, myList))
print(f'Using map with lambda: {myMap}')

def addOne(x):
    return x + 1
myMap = list(map(addOne, myList))
print(f'Using map with function: {myMap}')



"""
The Filter Function is used to filter out elements
from an iterable.
"""

myList = [1, 2, 3, 4, 5]
myFilter = list(filter(lambda x: x % 2 == 0, myList))
print(f'Using filter with lambda: {myFilter}')

def isEven(x):
    return x % 2 == 0
myFilter = list(filter(isEven, myList))
print(f'Using filter with function: {myFilter}')


"""
Filter and Map return iterators, they are lazy, meaning
they produce values only when needed.
Use the next() function to get the next value from an iterator.
"""

# Example using 'first' to utilize lazy evaluation
print(f'Finding the first even number: {next(filter(isEven, myList))}')

