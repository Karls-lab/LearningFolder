class Solution:
    # Roman numerals are written largest to smallest from left to right
    def romanToInt(self, s:str) -> int:
        lookup_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        priority_table = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
        total_count = 0
        for pos, roman_char in enumerate(s):
            if (pos + 1) < len(s): # check if a lower priority character is before a higher one
                if priority_table[s[pos+1]] > priority_table[s[pos]]:
                    total_count -= lookup_table[roman_char]
                    continue
            total_count += lookup_table[roman_char]
        return total_count


sol = Solution()
# print(sol.romanToInt("III"))
# print(sol.romanToInt("LVIII"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("MMXXIII"))