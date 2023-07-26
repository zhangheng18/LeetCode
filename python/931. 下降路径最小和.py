class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 备忘录,减少重复计算 最大正确值范围 -10000 - 10000 （n=100）
        self.memo = [[10001] * n for _ in range(n)]

        res = 10002
        for j in range(n):
            # 最后一行 的任意一列
            res = min(res, self.dp(matrix, n - 1, j))
        return res

    def dp(self, matrix, n, j):
        # 越界检查
        if n < 0 or j < 0 or n >= len(matrix) or j >= len(matrix):
            return 10002

        # 终止条件： 第一行
        if n == 0:
            return matrix[0][j]

        if self.memo[n][j] != 10001:
            return self.memo[n][j]

        # 转移方程： 对于 matrix[i][j]，只有可能从 matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1] 这三个位置转移过来。
        self.memo[n][j] = matrix[n][j] + min(
            self.dp(matrix, n - 1, j),
            self.dp(matrix, n - 1, j - 1),
            self.dp(matrix, n - 1, j + 1),
        )
        return self.memo[n][j]
