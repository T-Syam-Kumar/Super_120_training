def trappingwater(arr):
    l = 0
    r = len(arr)-1
    ans = 0
    lm = arr[0]
    rm = arr[-1]
    while l < r:
        if arr[l] < arr[r]:
            if arr[l] < rm:
                ans = max(ans, arr[l])
            else:
                ans = max(ans, rm)
            l+=1
        else:
            if arr[l] < rm:
                ans = max(ans, arr[l])
            else:
                ans = max(ans, rm)
            r -= 1
    return ans

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingwater(height))