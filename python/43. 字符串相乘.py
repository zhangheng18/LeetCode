class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """num1  num2  i * j = res[i + j, i + j + 1]"""
        num1_len, num2_len = len(num1), len(num2)
        res = [0] * (num1_len + num2_len)

        # 从个位数开始计算
        zero = ord('0')
        for i in range(num1_len - 1, -1, -1):
            for j in range(num2_len - 1, -1, -1):
                # 利用ascii码 转数字
                n1, n2 = ord(num1[i]) - zero, ord(num2[j]) - zero
                mul = n1 * n2
                p1, p2 = i + j, i + j + 1

                # 叠加到 res 上
                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # res 开头的0去掉
        i = 0
        while res[i] == 0 and i < len(res) - 1:
            i += 1
        # 转字符串
        return ''.join(map(str, res[i:])) or '0'
