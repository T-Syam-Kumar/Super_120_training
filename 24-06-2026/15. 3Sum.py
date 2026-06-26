class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if (i>0) and (nums[i] == nums[i-1]):
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k] 
                if sum > 0:
                    k-=1
                elif sum < 0:
                    j+=1
                else:
                    x = [nums[i],nums[j],nums[k]]
                    res.append(x)
                    j+=1
                    while (j<len(nums)) and nums[j] == nums[j-1]:
                        j+=1
        return res