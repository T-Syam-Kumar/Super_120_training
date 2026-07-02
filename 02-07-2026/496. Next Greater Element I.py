def nextGreaterElement(nums1, nums2):
    hash_table ={}
    stack = []
    res = [-1]*len(nums1)
    for i,val in enumerate(nums1):
        hash_table[val] = i
    for num in nums2:
        while stack and stack[-1]<num:
            temp = stack.pop()
            res[hash_table[temp]] = num
        if num in nums1 : 
            stack.append(num)
    return res