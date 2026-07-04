############################### Recursion ################################

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


######################## Memoization using Dictionary #####################

memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


######################## Memoization using Array ##########################

def fib(memo, n):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib(memo, n - 1) + fib(memo, n - 2)
    return memo[n]

n = 10
memo = [-1] * (n + 1)
ans = fib(memo, n)
print(ans)


######################## Using Built-in lru_cache #########################

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))


############################ Tabulation ##################################

def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(fib(10))


######################## Space Optimization ###############################

def fib(n):
    if n <= 1:
        return n
    f1,f2 = 1,1
    for i in range(2,n+1):
        res = f1+f2
        f1 = f2
        f2 = res
    return res

print(fib(10))