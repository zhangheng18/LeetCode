class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """a异或a=0 a异或0=a"""

        ret = 0
        # 异或n
        ret ^= len(nums)
        for i, num in enumerate(nums):
            # 索引和元素成对出现
            ret ^= i ^ num
        # 最后剩下的就是缺失的那个数
        return ret
