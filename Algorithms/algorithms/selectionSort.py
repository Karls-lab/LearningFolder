# A simple selection sort by Karl Poulson

import random
randomList = random.sample(range(0, 10, 1), 10)

print("List before sorting: " + str(randomList))

def selectionSort(A):
    # look through entire array for smallest number
    for i in range(len(A)):
        # print("Finding smallest...")
        # print(A[i::])
        # print(findSmallest(A[i::]))
        print(A[i::])
        smallestIndex = findSmallest(A[i::])
        tmp = A[i]
        A[i] = A[smallestIndex]
        A[smallestIndex] = tmp
    
    return A

# return index of smallest found integer
def findSmallest(A):
    smallest = A[0]
    smallestIndex = 0
    for i in range(len(A)):
        if A[i] < smallest:
            smallest = A[i]
            smallestIndex = i
    return smallestIndex

print(selectionSort(randomList))
print(findSmallest(randomList))