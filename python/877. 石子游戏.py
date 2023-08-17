from dataclasses import dataclass


@dataclass
class Pair:
    first: int
    second: int
    __solt__ = ('first', 'second')


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # # 先手 必胜（按索引的奇偶分为两组，即第 1、3 堆和第 2、4 堆，选最多的一堆）
        # return True

        return self.dp(piles) >= 0

    def dp(self, piles):
        n = len(piles)

        dp = [[Pair(0, 0) for _ in range(n)] for _ in range(n)]

        # base
        for i in range(n):
            dp[i][i].first = piles[i]
            dp[i][i].second = 0

        # dp[i][j] 用到dp[i+1][j]和 dp[i][j-1] 倒序遍历
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # 选左边
                left = piles[i] + dp[i + 1][j].second
                # 选右边
                right = piles[j] + dp[i][j - 1].second

                if left > right:
                    # Alice
                    dp[i][j].first = left
                    # Bob
                    dp[i][j].second = dp[i + 1][j].first
                else:
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j - 1].first
        res = dp[0][n - 1]
        return res.first - res.second
