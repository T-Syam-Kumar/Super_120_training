s = "abcbabdbabc"
ans = 0
i = 0
j = 2
for r in range(1,len(s)-1):
    while s[i] == s[j] and j < len(s) and i > -1:
        ans = max(ans, abs(j - i))
        i = i - 1
        j = j + 1
    i = r
    j = r+
print(ans)