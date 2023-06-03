class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums)
        return nums

    def sort(self, nums):
        # 避免内存反复分配
        self.temp = len(nums) * [0]
        self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums, lo, hi):
        # 归并排序
        if lo == hi:
            return

        mid = (lo + hi) // 2
        self._sort(nums, lo, mid)
        self._sort(nums, mid + 1, hi)
        self._merge(nums, lo, mid, hi)

    def _merge(self, nums, lo, mid, hi):
        l_start, r_start = lo, mid + 1

        temp = self.temp
        for i in range(lo, hi + 1):
            temp[i] = nums[i]

        for i in range(lo, hi + 1):
            # 左半数组合并完成
            if l_start == mid + 1:
                nums[i] = temp[r_start]
                r_start += 1
            # 右半数组合并完成
            elif r_start == hi + 1:
                nums[i] = temp[l_start]
                l_start += 1

            elif temp[l_start] < temp[r_start]:
                nums[i] = temp[l_start]
                l_start += 1
            else:
                nums[i] = temp[r_start]
                r_start += 1
