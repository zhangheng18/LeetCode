class Solution:
    def __init__(self):
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        # 备忘录 ，剪枝
        if expression in self.memo:
            return self.memo[expression]

        for idx, ch in enumerate(expression):
            if ch in ('+', '-', '*'):
                # 分治: 按运算符 分左右
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1 :])

                for a in left:
                    for b in right:
                        if ch == '+':
                            res.append(a + b)
                        elif ch == '-':
                            res.append(a - b)
                        elif ch == '*':
                            res.append(a * b)

        # 结束： 不含运算符， 解析数字
        if not res:
            res.append(int(expression))

        self.memo[expression] = res
        return res
