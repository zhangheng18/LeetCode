class Solution:
    def __init__(self):
        self.res = 0
        self.memo = []

    def numTrees(self, n: int) -> int:
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, lo, hi):
        if lo > hi:
            return 1
        if self.memo[lo][hi]:
            return self.memo[lo][hi]

        res = 0
        for mid in range(lo, hi + 1):
            left = self.count(lo, mid - 1)
            right = self.count(mid + 1, hi)
            res += left * right
        self.memo[lo][hi] = res
        return res
