class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_values = []
        for value in nums:
            if value not in unique_values:
                unique_values.append(value)
        return len(unique_values)
    
sol = Solution()
print(sol.removeDuplicates([0, 0, 0, 1, 1, 2, 2, 2, 2, 3]))


class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0 
        q = 1
        while q < len(nums):
            if nums[q] != nums[p]:
                nums[p+1] = nums[q]
                p += 1
            q += 1
        return p + 1
    
sol2 = Solution2()
print(sol2.removeDuplicates([0,0,0,1,1,1,2,2,2,3]))