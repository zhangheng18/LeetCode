class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)

        # dp[i][status] 第i+1天， 持有status=1 没持有 status=0 的 利润
        dp = [[0, 0] for _ in range(days)]

        # 第一天 初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]  # 最小

        for day in range(1, days):
            # day 天 没持有： 前天没持有 / 前天持有卖了
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][1] + prices[day])
            # day天持有: 前天持有 / 前天没持有 今天买入
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] - prices[day])

        return dp[days - 1][0]
