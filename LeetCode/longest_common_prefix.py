"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        strs.sort()
        longer = max(strs[0], strs[-1])
        shorter = min(strs[0], strs[-1])
        for count, char in enumerate(longer):
            if count == len(shorter):
                return longer[:count]
            if char != shorter[count]:
                return longer[:count]
        return longer


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["ab", "a"]))