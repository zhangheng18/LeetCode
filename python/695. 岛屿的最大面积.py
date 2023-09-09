class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """淹没陆地，返回最大的陆地面积"""
        m, n = len(grid), len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, i, j):
        # 越界 / 海水
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        # 淹没
        grid[i][j] = 0

        # 淹没与 (i, j) 相邻(上下左右)的陆地，并返回淹没的陆地面积
        return (
            self.dfs(grid, i - 1, j)
            + self.dfs(grid, i + 1, j)
            + self.dfs(grid, i, j - 1)
            + self.dfs(grid, i, j + 1)
            + 1
        )
