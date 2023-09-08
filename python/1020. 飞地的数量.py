class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """淹没靠边的陆地，数剩下的岛屿数量"""

        m, n = len(grid), len(grid[0])

        for i in range(m):
            # 左边
            self.dfs(grid, i, 0)
            # 右边
            self.dfs(grid, i, n - 1)

        for i in range(n):
            # 上边
            self.dfs(grid, 0, i)
            # 下面
            self.dfs(grid, m - 1, i)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res

    def dfs(self, grid: List[List[int]], i: int, j: int):
        """淹没 与i,j 相邻的岛屿"""
        # 结束：边界 海洋
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return

        # 填充
        grid[i][j] = 0

        # 上下左右
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
