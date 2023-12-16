class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        assert isinstance(x, int), "Input must be an integer"

        # Handle sign
        sign = 1 if x >= 0 else -1
        x = abs(x)

        # Reverse the digits
        reversed_x = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before updating the result
            if reversed_x > (INT_MAX - digit) // 10:
                return 0

            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x


sol = Solution()
# print(sol.reverse(123))
# print(sol.reverse(-123))
print(sol.reverse(900000))
print(sol.reverse(1534236469))
