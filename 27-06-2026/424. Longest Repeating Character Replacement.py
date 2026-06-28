def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}
        l = 0
        res = 0
        temp = 0
        for r in range(len(s)):
            mapp[s[r]] = mapp.get(s[r],0) + 1
            temp = max(mapp[s[r]],temp)
            if (r-l+1)-temp>k:
                mapp[s[l]] -= 1
                l += 1
            res = max(res,(r-l)+1)
        return res