class Solution:
    def __init__(self):
        self.res = []
        self.target_sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序 以去重
        candidates.sort()

        track = []
        self.backtrack(candidates, 0, track, target)
        return self.res

    def backtrack(self, nums: List[int], start: int, track: List[int], target: int):
        if self.target_sum == target:
            # 找到目标
            self.res.append(track[:])
            return
        if self.target_sum > target:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                # 剪枝重复的路径 只遍历第一次
                continue
            # 做选择
            self.target_sum += nums[i]
            track.append(nums[i])

            self.backtrack(nums, i + 1, track, target)

            self.target_sum -= nums[i]
            track.pop()
