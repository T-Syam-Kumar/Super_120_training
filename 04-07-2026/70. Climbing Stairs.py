def climbStairs(n):
    if n <= 1:
        return n
    f1,f2 = 1,1
    for i in range(2,n+1):
        res = f1+f2
        f1 = f2
        f2 = res
    return res

