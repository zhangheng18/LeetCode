class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        for i in range(len(nums)):
            for j in range(i):
                # 如果比 前面的大
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # # 二分查找解法
        # top = [0] * len(nums)
        # piles = 0
        #
        # for i in range(len(nums)):
        #     poker = nums[i]
        #
        #     # 查找左侧边界
        #     left, right = 0, piles
        #     while left < right:
        #         mid = (left + right) // 2
        #         if top[mid] < poker:
        #             left = mid + 1
        #         elif top[mid] > poker:
        #             right = mid
        #         else:
        #             right = mid
        #     # 没找到，新建堆
        #     if left == piles:
        #         piles += 1
        #
        #     top[left] = poker
        # return piles
