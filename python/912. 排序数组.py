import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.merge_sort(nums)
        return self.quick_sort(nums)

    @staticmethod
    def merge_sort(nums):
        # 归并排序

        # 初始化临时数组
        temp = [0] * len(nums)

        def merge(nums, lo, mid, hi):
            # 赋值 temp
            temp[lo : hi + 1] = nums[lo : hi + 1]

            i, j = lo, mid + 1
            for p in range(lo, hi + 1):
                # 左边数组已经遍历完
                if i > mid:
                    nums[p] = temp[j]
                    j += 1
                # 右边数组已经遍历完
                elif j > hi:
                    nums[p] = temp[i]
                    i += 1
                # 左边数组的值大于右边数组的值 取右边数组的值
                elif temp[i] > temp[j]:
                    nums[p] = temp[j]
                    j += 1
                else:
                    nums[p] = temp[i]
                    i += 1

        def sort(nums, lo, hi):
            if lo == hi:
                return
            mid = (lo + hi) // 2
            sort(nums, lo, mid)
            sort(nums, mid + 1, hi)
            merge(nums, lo, mid, hi)

        sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums):
        # 快速排序
        if len(nums) <= 1:
            return nums

        # 随机选择pivot 分区点
        pivot = random.choice(nums)

        # 三路快排， 避免相同值的元素过多导致的退化
        left = self.quick_sort([x for x in nums if x < pivot])
        right = self.quick_sort([x for x in nums if x > pivot])
        return left + [x for x in nums if x == pivot] + right
