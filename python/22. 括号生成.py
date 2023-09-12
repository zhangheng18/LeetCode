class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = ''
        self.backtrack(n, n, track, res)
        return res

    def backtrack(self, left: int, right: int, track: str, res: List[str]):
        # 不合法 先放左括号，剩余多
        if left > right:
            return

        # 不合法
        if left < 0 or right < 0:
            return
        # 结束
        if left == 0 and right == 0:
            res.append(track)
            return

        # 选择左括号
        track += '('
        self.backtrack(left - 1, right, track, res)
        track = track[:-1]

        # 选择右括号
        track += ')'
        self.backtrack(left, right - 1, track, res)
        track = track[:-1]
