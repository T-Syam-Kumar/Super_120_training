def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        maxx = [nums[0],max(nums[0],nums[1])]
        for i in range(2,n):
            curr = max(nums[i] + maxx[i-2], maxx[i-1])
            maxx.append(curr)
        return maxx[-1]