class Solution:
    # Roman numerals are written largest to smallest from left to right
    def romanToInt(self, s:str) -> int:
        lookup_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(12345))