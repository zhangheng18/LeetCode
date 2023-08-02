class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 滑动窗口
    #
    #     left, right = 0, 0
    #     windows, max_value = 0, float('-inf')
    #
    #     while right < len(nums):
    #         # 扩大窗口
    #         windows += nums[right]
    #         right += 1
    #         max_value = max(max_value, windows)
    #         # 减小窗口
    #         while windows < 0:
    #             windows -= nums[left]
    #             left += 1
    #
    #     return max_value

    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 表示以 nums[i] 结尾的最大子序和
        n = len(nums)
        if n == 0:
            return 0
        # 第一个元素前面 没有子数组
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
