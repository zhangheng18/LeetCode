class Solution:
    def hammingWeight(self, n: int) -> int:
        """n & (n−1)，其运算结果恰为把 nnn 的二进制位中的最低位的 1 变为 0 之后的结果"""
        cnt = 0
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt
