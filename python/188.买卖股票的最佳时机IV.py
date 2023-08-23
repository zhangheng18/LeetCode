class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 1:
            return 0

        if k > n // 2:
            # 买 卖 为一次交易， k大于这个值，相当于 不限次数交易
            return self.maxProfit_k_inf(prices)

        # dp[i][j][s] 第i天，交易次数j， 持有状态s=0 不持有， s=1 持有 的最大利润
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        # base
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')

        # 初始化买入
        for i in range(k, 0, -1):
            dp[0][i][1] = -prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                # i天 j次 不持有： i-1天j次不持有， i-1天j次持有卖出
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # i天j次 持有: i-1天k次持有， i-1天 j-1次 不持有 买入
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfit_k_inf(self, prices: List[int]) -> int:
        n = len(prices)

        ## dp[i][j] 第i天 持有状态j=0 不持有， j=1 持有 的最大利润
        # dp = [[0, 0] for _ in range(n)]
        #
        # # base
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        #
        # for i in range(1, n):
        #     # 不持有： 前一天不持有， 前一天持有卖了
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     # 持有： 前一天持有， 前一天不持有 今天买入
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        # return dp[n - 1][0]

        ## 优化内存占用
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0
