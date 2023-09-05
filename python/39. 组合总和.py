class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 加速
        candidates.sort(reverse=True)
        self.backtrack(candidates, target, [], 0, 0)
        return self.res

    def backtrack(self, nums: List[int], target, track: List[int], start, cur_total):
        # 结束
        if cur_total == target:
            self.res.append(track[:])
            return

        # 结束
        if cur_total > target:
            return

        for i in range(start, len(nums)):
            track.append(nums[i])
            cur_total += nums[i]
            # 可重复
            self.backtrack(nums, target, track, i, cur_total)

            track.pop()
            cur_total -= nums[i]
