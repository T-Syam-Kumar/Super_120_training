def consecutiveSetBits(self, n: int) -> bool:
        x = n & (n>>1)
        return x>0 and not x&(x-1)
n = int(input())
print(consecutiveSetBits(n))
