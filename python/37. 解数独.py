class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)

    def backtrack(self, board, i, j):
        m, n = 9, 9

        # 最后一列，开始下一行
        if j == n:
            return self.backtrack(board, i + 1, 0)

        # 最后一行,可行解
        if i == m:
            return True

        # 有预设数,下一个
        if board[i][j] != '.':
            return self.backtrack(board, i, j + 1)
        # 填充
        for ch in range(1, 10):
            ch = str(ch)
            # 不合法
            if not self.isValid(board, i, j, ch):
                continue

            # 选择 回溯
            board[i][j] = ch
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = '.'
        return False

    def isValid(self, board, row, col, ch):
        """判断是否可填充"""

        for i in range(9):
            # 行
            if board[row][i] == ch:
                return False

            # 列
            if board[i][col] == ch:
                return False

            # 所在3*3 方格
            if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == ch:
                return False
        return True
