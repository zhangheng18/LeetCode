class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0

        # 初始化棋盘
        board = [['.'] * n for _ in range(n)]

        # 放置 第一行
        self.backtrack(board, 0)

        return self.cnt

    def backtrack(self, board, row):
        # 最后一行 结束
        if row == len(board):
            # 一种方式
            self.cnt += 1
            return

        for col in range(len(board)):
            # 是否可放置
            if not self.valid(board, row, col):
                continue

            # 选择
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            # 取消选择
            board[row][col] = '.'

    @staticmethod
    def valid(board, row, col):
        """判罚是否可放置皇后"""

        # 列
        for i in range(row + 1):
            if board[i][col] == 'Q':
                return False

        # 右上
        r, c = row - 1, col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        # 左上
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        return True
