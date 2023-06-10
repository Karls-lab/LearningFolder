class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a.encode(), 2)
        b = int(b.encode(), 2)
        print(a)
        print(b)
        total = a + b
        binary = str(format(total, 'b'))
        return binary


sol = Solution()
print(sol.addBinary("11", "1"))