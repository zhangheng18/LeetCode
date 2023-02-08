class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >  n/2:
            # 两天才能交易一次， 即为没有k的限制
            return self.maxProfitInf(prices)
            
        dp = [ [ [0,0] for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] =  float('-inf')
        
        for i in range(n):
            for ck in range(k,0, -1):
                if i -1== -1:
                    dp[i][ck][0] = 0
                    dp[i][ck][1] = -prices[i]
                    continue
                dp[i][ck][0] = max( dp[i-1][ck][0], dp[i-1][ck][1] + prices[i])
                dp[i][ck][1] = max(dp[i-1][ck][1], dp[i-1][ck-1][0] - prices[i])
        return dp[n-1][k][0]

    def maxProfitInf(self, prices:List[int])->int:
        n = len(prices)
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1,n):
            tmp  = dp_0 
            dp_0 = max( dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, tmp - prices[i])
        return dp_0


