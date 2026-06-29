from math import ceil
def eating(arr,hrs):
    l = 0
    r = max(arr)
    ans = 0
    while l <= r:
        mid = (l+r)//2
        hr = 0
        for x in arr:
            hr += ceil(x/mid)
        if hr <= hrs:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans