
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascalsTriangle = []
        for x in range(1, numRows + 2):
            row = []
            for y in range(x):
                if y == 0 or y == x - 1:
                    row.append(1)
                else:
                    prev_row = pascalsTriangle[x-2]
                    row.append(prev_row[y-1] + prev_row[y])
            pascalsTriangle.append(row)
        return pascalsTriangle[numRows]

Sol = Solution()
print(Sol.generate(0))
print(Sol.generate(1))
pascalsTriangle = Sol.generate(3)
print(pascalsTriangle)
#