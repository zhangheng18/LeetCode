class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 发现一个岛屿
                    res += 1
                    # 淹没相邻的所有岛屿
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid: List[List[str]], i, j):
        """遍历上下左右相邻的岛屿 填充为海水"""
        # 结束： 超出边界, 遇到海水
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i - 1, j)  # 上
        self.dfs(grid, i + 1, j)  # 下
        self.dfs(grid, i, j - 1)  # 左
        self.dfs(grid, i, j + 1)  # 右
