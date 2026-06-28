class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        res=[0,s[0]]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                x=s[i:j+1]
                if x==x[::-1]:
                    if len(x)>res[0]:
                        res[0]=len(x)
                        res[1]=x
        return res[1]