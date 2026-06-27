def longestConsecutive(nums):
        hash_set = set(nums)
        res = 0
        for num in hash_set:
            if (num-1) not in hash_set:
                count = 0
                while (num + count) in hash_set:
                    count+=1
                res = max(count,res)
        return res
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))