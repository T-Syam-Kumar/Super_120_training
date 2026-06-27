def two_sum2(nums,k):
    res = []
    i,j = 0,len(nums)-1
    while i<j:
        if nums[i]+nums[j] == k:
            res = [i+1,j+1]
            break
        if nums[i]>k:
            i+=1
        else:
            j-=1
    return res
numbers = [2,7,11,15]
target = 9
print(two_sum2(numbers,target))