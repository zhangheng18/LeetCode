class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 插入次数
        res = 0

        # 需要的右括号数量
        need = 0
        for c in s:
            if c == '(':
                need += 1
            if c == ')':
                need -= 1
                # 右括号多了
                if need == -1:
                    res += 1
                    need = 0

        return res + need
