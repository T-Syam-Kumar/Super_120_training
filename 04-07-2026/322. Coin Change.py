#******************************** Brute Force*********************************

def coinChange(coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        min_count = float('inf')
        
        for coin in coins:
            res = coinChange(coins, amount - coin)
            if res != -1:
                min_count = min(min_count, 1 + res)
                
        return min_count if min_count != float('inf') else -1

#******************************** Memoization **********************************

def coinChange(coins,amount):
        memo = {}
        
        def solve(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            
            min_count = float('inf')
            
            for coin in coins:
                res = solve(rem - coin)
                if res != -1:
                    min_count = min(min_count, 1 + res)
            
            memo[rem] = min_count if min_count != float('inf') else -1
            return memo[rem]
            
        return solve(amount)

#********************************** Tabulation ********************************

def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will be storing the minimum number of coins required for amount i
        # amount + 1 is a placeholder for infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1