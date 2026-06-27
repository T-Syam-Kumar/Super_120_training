# 1. Single number XOR basics
arr = [1,2,3,2,1]
res = 0
for i in arr:
    res ^= i
print(res)

# 2. Missing Number XOR + Range Numbers
arr = [1,4,3,5,0]
res = 0
for i in range (len(arr)):
    res ^= arr[i]^i
print(res^len(arr))

# 3. Number of 1 Bits (Hamming Weight)
n = 11
cnt = 0
while n:
    cnt += n&1
    n >>= 1
print(cnt)

# 4. power of 2
n = 8
print(False if n&(n-1) else True)

# 5. Reverse Bits
n = 11
res = 0
for _ in range(32):
    res = res << 1
    res = res | (n&1)
    n >>= 1
print(res)

# 6. Subset(power set) bit Masking




































# 6 Subsets (Power Set)    Bit Masking
            # num = [1,2,3]
            # n = len(num)
            # res = []
            # for mask in range(1<<n):
            #     sublist =[]
            #     for i in range(n):
            #         if (mask & 1) == 1:
            #             sublist.append(num[i])
            #         mask >>= 1
            #     res.append(sublist)
            # print(res)
