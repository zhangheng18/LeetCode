from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: deque) -> int:
            stack = []
            num = 0
            sign = '+'
            while s:
                n = s.popleft()
                if n.isdigit():
                    # 字符转整数
                    num = num * 10 + int(n)

                if n == '(':
                    # 遇到左括号，递归计算
                    num = helper(s)

                # 遇到符号 / 结束 入栈
                if ((not n.isdigit()) and n != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    # 重置符号
                    sign = n
                    num = 0

                if n == ')':
                    # 遇到右括号，停止递归，返回计算结果
                    break

            # 计算结果
            return sum(stack)

        return helper(deque(s))
