#Create n empty buckets (Or lists).
#2) Do following for every array element arr[i].
#.......a) Insert arr[i] into bucket[n*array[i]]
#3) Sort individual buckets using insertion sort.
#4) Concatenate all sorted buckets.

# https://en.wikipedia.org/wiki/Combination for the n choose k 
# n choose k: n!/(k!(n-k)!)

# Python3 program to sort an array
# using bucket sort
def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucketSort(unsorted_list):
	print(f"Bucket Sorting x: {unsorted_list}")
	arr = []
	buckets = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(buckets):
		arr.append([])
		
	# Put array elements in different buckets
	for element in unsorted_list:
		index_b = int(buckets * element)
		arr[index_b].append(element)
	
	# Sort individual buckets
	for i in range(buckets):
		arr[i] = insertionSort(arr[i])
		
	# concatenate the result
	k = 0
	for i in range(buckets):
		for j in range(len(arr[i])):
			unsorted_list[k] = arr[i][j]
			k += 1
	return unsorted_list

# Driver Code
x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

# This code is contributed by
# Oneil Hsiao
