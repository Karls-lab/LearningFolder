"""The zip() function takes iterables iter_1, iter_2, ... iter_n, 
    and aggregates them into a single iterable by aligning the 
    i-th values into a single tuple. The result is an iterable of tuples."""

# Example 1:
list_0 = [1,2,3]
list_1 = [4,5,6]
# [(1,4), (2,5), (3,6)]
zipped = (list(zip(list_0, list_1)))
print(zipped)

# Unzip to lists again
# The * is used to unpack all elements of the list. Removes the 
# outer brackets of the list
list_0, list_1 = zip(*zipped)
print(list(list_0))
print(list(list_1))

# Unpacking example:
nums = [1,2,3,4,5,6]
def num_sum(*args):
    return sum(args)
print(num_sum(*nums))


# Zipping tuples into a dictionary 
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
            ('Bob', 99000, 'mid-level manager'),
            ('Frank', 87000, 'CEO')]
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)

# Note: zip only needs to take in iterables, so that means dicts and tuples