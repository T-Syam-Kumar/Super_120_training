############# Tabulation #########################

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max(nums[i]+dp[i-2],nums[i-1])
    return dp[-1]


############ Space optimisation ############

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    x = nums[0]
    y = max(nums[1],nums[0])
    for i in range(2,n):
        cur = max(nums[i] + x,y)
        x = y
        y = cur
    return y 


############ Another Approach ####################

def rob(nums):
    r1,r2 = 0,0
    for i in nums:
        temp = max(i+r1,r2)
        r1 = r2
        r2 = temp
    return r2
