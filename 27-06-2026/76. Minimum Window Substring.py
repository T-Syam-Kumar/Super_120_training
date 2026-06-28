class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1,-1]
        found = 0
        len_res = float('inf')
        count_t = {}      
        count_s = {}
        for i in t:
            count_t[i] = count_t.get(i,0) + 1
        i = 0
        total = len(count_t)
        for j in range(len(s)):      
            curr_val = s[j]
            if curr_val in count_t:
                count_s[curr_val] = count_s.get(curr_val,0) + 1
            if curr_val in count_t and  count_t[curr_val] == count_s[curr_val]:
                found += 1
            while  found == total:
                if ((j-i)+1) < len_res:
                    len_res = ((j-i)+1)
                    res = [i,j]
                if s[i] in count_s:
                    count_s[s[i]] -=1
                if s[i] in count_t and count_s[s[i]] < count_t[s[i]]:
                    found -= 1
                i+=1
        i,j = res 
        return s[i:j+1] if len_res != float('inf') else ''