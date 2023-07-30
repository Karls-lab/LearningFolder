"""
I can either climb 1 or 2 steps at a time. n = 4
Possible combinations: 1, 1, 2 or 1, 2, 1 or 2, 1, 1 or 2, 2
Would the solution be 2 ** n?

n = 1, 1
1 

n = 2, 2
1, 1 or 2 

n = 3, 3
1, 1, 1 or 1, 2 or 2, 1

n = 4, 5
1, 1, 1, 1 or 1, 1, 2 or 1, 2, 1 or 2, 1, 1 or 2, 2

n = 5, 8
1, 1, 1, 1, 1 or 1, 1, 1, 2 or 1, 1, 2, 1 or 1, 2, 1, 1 or 2, 1, 1, 1 or 1, 2, 2 or 2, 1, 2 or 2, 2, 1

Reucurrence Relation:
T(n) = T(n-1) + T(n-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        sol = [1, 2]
        for i in range(2, n):
            sol.append(sol[i-1] + sol[i-2])
        return sol[n-1]

sol = Solution()
print(sol.climbStairs(5))