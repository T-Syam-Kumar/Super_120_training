def search(nums,target):
    def first():
        res = -1
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return res
    
    def last():
        res = -1
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                l = m+1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return res
    return [first,last]

nums = [5,7,7,8,8,10]
target = 8
ans = search(nums,target)
print(ans)