class Solution:
    def fib(self, n: int) -> int:
        # n < 2
        if n == 0 or n == 1:
            return n

        # dp[i-1] , dp[i-2]
        dp_i_1, dp_i_2 = 1, 0

        # n = (n-1) + (n-2)
        for i in range(2, n + 1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i_1
