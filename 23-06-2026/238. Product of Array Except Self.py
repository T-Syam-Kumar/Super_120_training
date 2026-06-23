nums = [1,3,12,6]
n = len(nums)
res = [1] * n
l = r = 1
for i in range(n):
    res[i] = l
    l *= nums[i]
for j in range(n-1,-1,-1):
    res[j] *= r
    r *= nums[j]
