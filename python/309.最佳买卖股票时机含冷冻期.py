class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)

        if days < 2:
            return 0

        # dp[i][j]= 第 i天 j=0 持有股票， j=1 不持有股票  的最大利润
        dp = [[0, 0] for _ in range(days)]

        # base
        # 第1天
        dp[0][0] = 0  # 不持有
        dp[0][1] = -prices[0]  # 第1天价格买入

        # 第2天
        # 前一天没持有， 或者持有 但是卖出
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])  #
        # 前一天持有， 第2天价格买入
        dp[1][1] = max(dp[0][1], -prices[1])

        # 第三天 。。。。
        for i in range(2, days):
            # 前一天 没有 ， 或者前一天有 卖了
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            # 前一天 有， 前2天没有（冷冻期） - 买入价格
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        # 最后一天 卖出状态 利润最大
        return dp[days - 1][0]
