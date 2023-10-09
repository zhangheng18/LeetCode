class Solution:
    def minInsertions(self, s: str) -> int:
        # 插入次数
        res = 0
        # 需要右括号个数
        need = 0

        for c in s:
            if c == '(':
                need += 2
                if need % 2:
                    # 插入一个右括号
                    res += 1
                    # 需要的右括号减一
                    need -= 1
            elif c == ')':
                need -= 1
                # 右括号多了
                if need == -1:
                    # 插入左括号
                    res += 1
                    # 补充一个右括号
                    need = 1

        return res + need
