# Even number or not ?
n = 4
print("even") if n & 1 == 0 else print("odd")
# no of set bits
n = 5
cnt = 0
while n>0:
    cnt += n&1
    n >>= 1
print(cnt)
# no of reset bits
n = 5
cnt = 0
while n>0:
    cnt += n&1
    n >>= 1
print(cnt)