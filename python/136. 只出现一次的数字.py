class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """一个数和它本身做异或运算结果为 0，即 a ^ a = 0；一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a"""
        ret = 0
        for num in nums:
            ret ^= num
        return ret
