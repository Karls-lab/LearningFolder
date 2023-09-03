
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascalsTriangle = []
        for x in range(1, numRows + 1):
            row = []
            for y in range(x):
                if y == 0 or y == x - 1:
                    row.append(1)
                else:
                    prev_row = pascalsTriangle[x-2]
                    row.append(prev_row[y-1] + prev_row[y])
            pascalsTriangle.append(row)
        return pascalsTriangle

Sol = Solution()
pascalsTriangle = Sol.generate(10)
print(pascalsTriangle)
# input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
