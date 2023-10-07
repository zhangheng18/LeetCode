class Solution:
    def isValid(self, s: str) -> bool:
        """利用栈做匹配"""
        stack = []

        map_dic = {')': '(', '}': '{', ']': '['}
        for c in s:
            # 左括号入栈
            if c not in map_dic:
                stack.append(c)
            else:
                # 右括号匹配
                if stack and map_dic[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        # 栈为空则匹配成功
        return not stack
