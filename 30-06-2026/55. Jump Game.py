def canJump(nums) :
        d = len(nums)-1
        for i in range(d-1,-1,-1):
            if (i+nums[i])>=d:
                d = i
        return d == 0