def isSubsequence(s: str, t: str) -> bool:
    s = list(s)
    for character in t:
        if s and character == s[0]:
            print("popping", s[0])
            s.pop(0)
    return True if len(s) == 0 else False



s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
print(isSubsequence("axc", "ahbgdc"))