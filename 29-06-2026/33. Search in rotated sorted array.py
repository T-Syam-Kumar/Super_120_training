def search(arr,key):
    l = 0
    r = len(arr)-1
    res = -1
    while l <= r:
        m = (l+r)//2
        if arr[m] == key:
            return m
        # left side
        if arr[m] >= arr[l]:
            if arr[l] <= key < arr[m]:
                r = m - 1
            else:
                l = m + 1
        # right side
        else:
            if arr[m]<key<=arr[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
nums = [4,5,6,7,0,1,2]
target = 0