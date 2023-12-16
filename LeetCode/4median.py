import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2) # In place
        return statistics.median(nums1)


sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))
