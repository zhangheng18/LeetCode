class Solution:
    MAX_VALUE = float('inf')
    IGNORE_VAL = -1

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 备忘录
        self.memo = [[self.IGNORE_VAL] * n for _ in range(m)]

        return self.dp(grid, m - 1, n - 1)

    def dp(self, grid, m, n):
        if m == 0 and n == 0:
            return grid[0][0]

        # 越界
        if m < 0 or n < 0:
            return self.MAX_VALUE

        # 已经计算过
        if self.memo[m][n] != self.IGNORE_VAL:
            return self.memo[m][n]

        self.memo[m][n] = (
            min(self.dp(grid, m - 1, n), self.dp(grid, m, n - 1)) + grid[m][n]
        )

        return self.memo[m][n]
