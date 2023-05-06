# A string is isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    else:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            if t[i] not in t_dict:
                t_dict[t[i]] = s[i]
            if s_dict[s[i]] != t[i] or t_dict[t[i]] != s[i]:
                return False
        return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("ab", "aa"))
print(isIsomorphic("ab", "ca"))
print(isIsomorphic("ab", "cc"))
print(isIsomorphic("ab", "cd"))
print(isIsomorphic("ab", "ef"))
