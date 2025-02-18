class Solution:
    def isValid(self, s: str) -> bool:
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0
    
sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
