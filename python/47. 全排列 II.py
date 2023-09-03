class Solution:
    def __init__(self):
        self.used = []
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 排序方便去重
        nums.sort()

        self.used = [False] * len(nums)
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums: List[int], track: List[int]):
        n = len(nums)
        if len(track) == n:
            self.res.append(track[:])
            return

        for i in range(n):
            # 剪枝 使用过
            if self.used[i]:
                continue

            # 保持相对位置 剪枝
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue

            # 选择
            self.used[i] = True
            track.append(nums[i])
            self.backtrack(nums, track)
            self.used[i] = False
            track.pop()
