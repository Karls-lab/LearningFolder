class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join([c for c in s.lower() if c.isalnum()])
        return cleaned_str == cleaned_str[::-1]
    
sol = Solution
sol.isPalindrome("")