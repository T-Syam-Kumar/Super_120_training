def subarray(nums,k):
    dic = {0:1}
    ps = 0 # prefix sum
    ans = 0
    for n in nums:
        ps += n
        temp = ps - k
        if temp in dic:
            ans += dic[temp]
        dic[ps] = dic.get(ps,0) + 1
    return ans

arr = [1,1,1]
n = 2
print(subarray(arr,n))


# Palindrome
n = 9876
ans = 0
while n > 0:
    ans = ans*10 + (n%10)
    n = n // 10
print(ans)

