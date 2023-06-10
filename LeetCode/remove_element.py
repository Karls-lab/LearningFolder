class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        filtered_list = filter(lambda x: x != val, nums)
        return len(list(filtered_list))
    
sol = Solution()
print(sol.removeElement([3,2,2,3], 3))