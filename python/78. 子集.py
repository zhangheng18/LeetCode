from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums: List[int], start: int, track: List[int]):
        """回溯"""

        # 前序
        self.res.append(track[:])

        for i in range(start, len(nums)):
            # 做选择
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            # 撤销选择
            track.pop()
