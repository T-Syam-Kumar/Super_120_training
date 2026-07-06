class Solution:
    def rob(nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums1 = nums[1:]
        nums2 = nums[:-1]
        def cal(nums):
            r1,r2 = 0,0
            for i in nums:
                temp = max(i+r1,r2)
                r1 = r2
                r2 = temp
            return r2
        res1 = cal(nums1)
        res2 = cal(nums2)
        return max(res1,res2)