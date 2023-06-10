from ast import List


def pivotIndex(nums: List) -> int:
    for count, value in enumerate(nums):
        left_array = nums[:count]
        right_array = nums[count+1:]
        print(f"Left: {left_array}")
        print(f"Right: {right_array}")
        if sum(left_array) == sum(right_array):
            return count 
        print("")
    return -1


list1 = [4, 2, 6, 2, 1, 2, 4, 9]
list2 = [1,7,3,6,5,6]
print(pivotIndex(list2))