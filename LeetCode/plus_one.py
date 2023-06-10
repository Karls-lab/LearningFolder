class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        total = 0
        digits.reverse()
        for index, num in enumerate(digits):
            total += (10 ** index) * num
        total += 1
        total = str(total)
        return_list = []
        for character in total:
            return_list.append(int(character))
        return return_list

sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([1, 9, 9]))
print(sol.plusOne([9]))

