def isAnagram( s,t):
        Dict_s = {}
        Dict_t = {}
        for i in range(len(s)):
            Dict_s[s[i]] = Dict_s.get(s[i], 0) + 1
            Dict_t[t[i]] = Dict_t.get(t[i], 0) + 1
        return Dict_s == Dict_t
s = input()
t = input()
ans = isAnagram(s, t)
print(ans)