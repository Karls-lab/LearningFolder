# Given a list of numbers, and a target number.
# Return indices where the two numbers add up to the target.

"""
For each element in the list, sum that element with all other elements one at at time,
except for itself. If the sum is equal to the target, return the indices of the two elements.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i_pos, i in enumerate(nums):
            for j_pos, j in enumerate(nums):
                if i_pos != j_pos:
                    print(i + j)
                    if i + j == target:
                        print(i_pos, j_pos)
                        return [i_pos, j_pos]
                    
class Solution_hash:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for index, element in enumerate(nums):
            if element in hash_map:
                # If the difference between the target and the current element is in the hash map
                return [index, hash_map[element]]
            else:
                # Calculates the difference between the target and the current element
                hash_map[target - element] = index

sol = Solution_hash()
sol.twoSum([2,7,11,15], 9)