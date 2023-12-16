"""
The sorted() method is a powerful python method that can be used 
to sort any iterable, such as lists, tuples, dictionaries, etc.
It uses the Timsort algorithm, O(n log n) time complexity.
"""
import math 
import random

# Example 1: Sort a list random numbers
numbers = [random.randint(0, 9) for _ in range(10)]
print(f"\nUnsorted: {numbers}")
print(f"Sorted: {sorted(numbers)}")


# Example 2: Sort a list of strings
strings = ["a", "c", "b", "d"]
print(f"\nUnsorted: {strings}")
print(f"Sorted: {sorted(strings)}")


# Example 3: Sort a Dictionary by a key 
people = {1: 'James', 2: 'John', 3: 'Adam', 4: 'Bob'}
print(f"\nUnsorted: {people}")
print(f"Sorted by Values: {sorted(people.values(), key=lambda x: x)}")
print(f"Sorted by Keys: {sorted(people.keys(), key=lambda x: x)}")
print(f"Sorted by Name: {sorted(people.items(), key=lambda x: x[1])}")

# Example 3: Sort a Dictionary by a key 
# blackLibraryRecords = {'firstName': 'Caiphus',
#                     'lastName': "Cain",
#                     'age': 28,
                    # 'Rank': 'Commissar'}

# print(f"\nDefault: {sorted(blackLibraryRecords)} ")
# print(f'\nSorted by key: {sorted(blackLibraryRecords, key=)}')

