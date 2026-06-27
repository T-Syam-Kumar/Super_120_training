nums = [1,2,3,1]
flag = 0
seen = set()
for num in nums:
    if num in seen:
        flag = 1
    else:
        seen.add(num)
print(True if flag == 1 else False)
print(True if len(set(nums)) - len(nums) else False)