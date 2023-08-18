class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     days = len(prices)
    #
    #     # dp[i][status] 第i+1天， 持有status=1 没持有 status=0 的利润
    #     dp = [[0, 0] for _ in range(days)]
    #
    #     # 第1天
    #     dp[0][0] = 0
    #     dp[0][1] = -prices[0]  # 不可能持有，取个最小值
    #
    #     for i in range(1, days):
    #         # 不持有： 前一天没有   / 前一天有但是卖了
    #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    #
    #         # 持有：   前一天有 / 买入
    #         dp[i][1] = max(dp[i - 1][1], -prices[i])
    #
    #     # 最后一天 不持有 利润最大
    #     return dp[days - 1][0]
    def maxProfit(self, prices: List[int]) -> int:
        # 找到最小价格，假设买入， 然后找到最大价格，假设卖出
        min_price = float('-inf')
        max_price = 0
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)
        return max_price
