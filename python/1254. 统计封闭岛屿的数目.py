class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """先把靠边的岛屿淹没，剩下的就是封闭岛屿"""

        m, n = len(grid), len(grid[0])

        for i in range(m):
            # 左面
            self.dfs(grid, i, 0)
            # 右面
            self.dfs(grid, i, n - 1)

        for i in range(n):
            # 上面
            self.dfs(grid, 0, i)
            # 下面
            self.dfs(grid, m - 1, i)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        """从 (i, j) 开始，将与之相邻的陆地都变成海水"""

        # 结束:边界 / 是海
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 1:
            return

        # 填充为海水
        grid[i][j] = 1

        # 上下左右填充
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
