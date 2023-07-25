import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        height = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # 二分查找发
        top = [0] * len(nums)
        piles = 0

        for i in range(len(nums)):
            poker = nums[i]

            # 搜左侧边界 二分法
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] < poker:
                    left = mid + 1
                elif top[mid] > poker:
                    right = mid
                else:
                    right = mid

            if left == piles:
                piles += 1
            top[left] = poker
        return piles
