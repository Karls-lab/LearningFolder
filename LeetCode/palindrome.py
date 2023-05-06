class Solution:
    def isPalindrome(self, x: int) -> bool:
        # converts int to a string, and separates each character into a list
        list_x = [character for character in str(x)]
        if list_x[::-1] == list_x:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(12345))