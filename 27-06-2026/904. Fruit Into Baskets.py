def totalFruit(fruits,k):
        mapp = {}
        k = 2
        l = 0
        ans = 0
        total = 0
        for r in range(len(fruits)):
            total += 1
            mapp[fruits[r]] = mapp.get(fruits[r],0)+1
            while len(mapp)>k:
                total -= 1
                mapp[fruits[l]] -= 1
                if mapp[fruits[l]] == 0:
                    mapp.pop(fruits[l])
                l += 1
            ans = max(ans,total)
        return ans
arr = [1,2,1]
k = 2
print(totalFruit(arr,k))