from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯
        self.backtrack(n, 1, k, [])
        return self.res

    def backtrack(self, n: int, start: int, k: int, track: List[int]):
        if len(track) == k:
            # 结束
            self.res.append(track[:])
            return

        for i in range(start, n + 1):
            # 做选择
            track.append(i)
            self.backtrack(n, i + 1, k, track)
            # 撤销
            track.pop()
