class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1"""
        return False if n <= 0 else (n & (n - 1) == 0)
