import random 
from heapq import heappop, heappush


randomList = [0, 1, 2, 3]#random.sample(range(0, 9), 9)
print(randomList)

# root of tree is A[1]
# the recurrence relation: T(n) <= T(2n/3) + theta(1)
# by the master theorem, T(n) = O(lg n)

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))



# def parent(i):
#     return(i/2)

# def left(i):
#     return 2*i

# def right(i):
#     return (2*i) + 1


# def MAX_HEAPIFY(A, i):
#     l = left(i)
#     r = right(i)
#     print(i, r, l, A)
#     # check if r or l is out of range:
#     if l < len(A) and A[l] > A[i]:
#             largest = l 
#     else: largest = i 
#     if r <= len(A) and A[r] > A[largest]:
#         largest = r 
#     if largest != i:
#         temp = A[i] 
#         A[i] = A[largest]
#         A[largest] = temp
#         #MAX_HEAPIFY(A, largest)

# def BUILD_MAX_HEAP(A):
#     i = int(len(A) / 2)
#     for x in range(i):
#         value = i - x
#         MAX_HEAPIFY(A, value)


# BUILD_MAX_HEAP(randomList)
# root = randomList[0]
# index = randomList.index(root)
# print(f"root: {root}")
# print(f"left: {left(index)}")
# print(f"right: {right(index)}")