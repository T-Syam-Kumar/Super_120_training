class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        dp = [[0 for _ in range(W + 1)] for _ in range(n)]
        for j in range(W + 1):
            if wt[0] <= j:
                dp[0][j] = val[0]
        for i in range(1, n):
            for j in range(W + 1):
                if wt[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(val[i] + dp[i-1][j - wt[i]], dp[i-1][j])
        return dp[n-1][W]