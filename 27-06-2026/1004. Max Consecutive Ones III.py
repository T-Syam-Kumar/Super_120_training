def max_con(arr,k):
    l , r , ans = 0,0,0
    for r in range(len(arr)):
        if arr[r] == 0:
            ans += 1
        while  ans >k:
            if arr[l] == 0:
                ans -= 1
            l += 1
        ans = max(ans,r-l+1)
array = [1,1,1,0,0,0,1,1,1,1,0]
key = 2
print(max_con(array,key))