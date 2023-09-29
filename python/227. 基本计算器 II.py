from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: deque):
            stack = []
            sign = '+'
            num = 0

            while s:
                c: str = s.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    # 遇到左括号，递归计算
                    num = helper(s)

                if not c.isdigit() or len(s) == 0:
                    # 遇到符号 / 结束 入栈

                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))
                    # 重置符号
                    sign = c
                    num = 0

                if c == ')':
                    # 遇到右括号，停止递归，返回计算结果
                    break
            # 计算结果
            return sum(stack)

        return helper(deque(s.replace(' ', '')))
