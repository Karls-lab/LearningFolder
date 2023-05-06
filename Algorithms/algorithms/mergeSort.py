# Merge sort implementaion by Karl Poulson in Python
# Time complexity: big O( n log n)

testArray = [2, 8, 5, 3, 9, 4, 1, 7]


def mergeSort(a):
    print(a)
    if( len(a) <= 1): # If run size is <= 1, then do nothing
        print("DONE" + str(len(a)))
        return a

    middleIndex = (len(a)) // 2
    arrayOne = a[:middleIndex]
    arrayTwo = a[middleIndex:]
    #print(arrayOne)
    #print(arrayTwo)

    arrayOne = mergeSort(arrayOne)
    arrayTwo = mergeSort(arrayTwo)

    return merge(arrayOne, arrayTwo)

def merge(a, b):
    print("merging..." + str(a) + str(b))
    c = []
    while(len(a) > 0 and len(b) > 0):
        if( a[0] > b[0] ):
            c.append(b[0])
            del b[0]
        else:
            c.append(a[0])
            del a[0]
    # a or b will be empty
    while(len(a) != 0):
        c.append(a[0])
        del a[0]

    while(len(b) != 0):
        c.append(b[0])
        del b[0]

    print("Sorted array c: " + str(c))
    return c



#middleIndex = (len(testArray) - 1) // 2
#print(middleIndex)
#print(testArray[middleIndex + 1::])

sortedArray = mergeSort(testArray)
print(sortedArray)

# del testArray[0]
# print(testArray)
# print(testArray[0])