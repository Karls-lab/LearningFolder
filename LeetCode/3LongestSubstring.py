class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myList = []
        subString = {}
        for char in s:
            if char not in myList:
                myList.append(char)
            else:
                subString[str(myList)] = len(myList)
                myList = [char]

        subString[str(myList)] = len(myList)
        # print(f"my list: {myList}, len: {len(myList)}")
        print(subString)
        return max(subString.values())
        


# Finds the longest unique substring 
# 'abcabcbb' -> 'abc', return 3

sol = Solution()
# print(sol.lengthOfLongestSubstring('abcabcbb'))
# print(sol.lengthOfLongestSubstring('pwwkew'))
# print(sol.lengthOfLongestSubstring(""))
# print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("dvdf"))