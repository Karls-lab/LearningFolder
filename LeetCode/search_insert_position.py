class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, len(nums), 0, target)

    def binary_search(self, nums, high, low, target):
        if high >= low:
            mid = (high + low) // 2
            if target == nums[mid]:
                return mid 
            elif mid > target:  # middle is big, high is now mid
                self.binary_search(nums, mid - 1, low, target)
            else:               # middle is too small, low is now mid
                self.binary_search(nums, high, mid + 1, target)
        else:
            return -1


sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))