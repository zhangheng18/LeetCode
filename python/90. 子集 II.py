from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 排序
        nums.sort()

        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums, start, track):
        # 添加
        self.res.append(track[:])

        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i - 1] == nums[i]:
                continue

            # 做选择
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()
