class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_k, n = 2, len(prices)
        dp = [ [ [0,0] for _ in range(max_k+1) ] for _ in range(n)]
        
        for i in range(n):
            for k in range(max_k,0,-1):
                if i -1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][max_k][0]
