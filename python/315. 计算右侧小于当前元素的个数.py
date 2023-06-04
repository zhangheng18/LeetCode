from collections import namedtuple


class Solution:
    pair = namedtuple("Pair", ["id", "val"])

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.count = [0] * n
        self.temp = [0] * n

        self.arr = [self.pair(i, num) for i, num in enumerate(nums)]

        self.sort(self.arr, 0, n - 1)
        return self.count

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = (lo + hi) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        i, j = lo, mid + 1
        for p in range(lo, hi + 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
                self.count[nums[p].id] += j - mid - 1
            elif self.temp[i].val > self.temp[j].val:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
                self.count[nums[p].id] += j - mid - 1
