class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))
print(sol.isAnagram("aacc", "ccac"))
print(sol.isAnagram("ab", "a"))
print(sol.isAnagram("a", "ab"))