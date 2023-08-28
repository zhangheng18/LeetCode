class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        # 不能被等分
        if total % k:
            return False
        target = total // k

        # 降序排序 剪枝
        nums.sort(reverse=True)

        # # 初始化桶
        # bucket = [0] * k
        # return self.backtrack_nums(nums,0, bucket,target)

        used = 0
        self.memo = {}
        return self.backtrack_bucket(k, 0, nums, 0, used, target)

    # def backtrack_nums(self, nums, index, bucket, target):
    #     """数字选桶， 超时"""

    #     # 结束
    #     if index == len(nums):
    #         for i in bucket:
    #             if i != target:
    #                 return False
    #         return True

    #     for i in range(len(bucket)):
    #         # 超过 target 跳过
    #         if bucket[i] + nums[index] > target:
    #             continue

    #         # 选择
    #         bucket[i] += nums[index]

    #         #可行继续递
    #         if self.backtrack(nums, index+1, bucket, target):
    #             return True

    #         #撤销选择
    #         bucket[i] -= nums[index]

    #     #无解
    #     return False

    def backtrack_bucket(self, k, bucket, nums, start, used, target):
        """桶选数字"""
        if k == 0:
            # 所有桶 被装满
            return True
        if bucket == target:
            # 装满一个桶
            res = self.backtrack_bucket(k - 1, 0, nums, 0, used, target)
            self.memo[used] = res
            return res

        if used in self.memo:
            # 避免冗余计算
            return self.memo[used]

        for i in range(start, len(nums)):
            # 剪枝
            if ((used >> i) & 1) == 1:
                continue

            if bucket + nums[i] > target:
                continue

            # 做选择

            # 第i位 置为1
            used |= 1 << i

            bucket += nums[i]
            if self.backtrack_bucket(k, bucket, nums, i + 1, used, target):
                return True
            used ^= 1 << i  # 第i位置为0
            # 撤销选择
            bucket -= nums[i]

        # 无解
        return False
