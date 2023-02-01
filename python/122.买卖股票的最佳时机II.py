class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [ [0,0] ] * days

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1,days):
            dp[i][0] = max(  dp[i-1][0], dp[i-1][1]+ prices[i])
            dp[i][1] = max( dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[days-1][0]
