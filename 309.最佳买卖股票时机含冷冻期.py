class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        
        dp = [[0,0] for _ in range(days)]

        for i in range(days):
            if (i -1) == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if (i -2) == -1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1],-prices[i])
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[days-1][0]
