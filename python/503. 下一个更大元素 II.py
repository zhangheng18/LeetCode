class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [-1] * n

        stock = []
        #循环数组 遍历两遍 取余
        for i in range(2 * n):
            idx = i % n
            while stock and nums[stock[-1]] < nums[idx]:
                res[stock.pop()] = nums[idx]
            stock.append(idx)
        return res