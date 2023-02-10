class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo1 = [ -1 for _ in range(n)]
        memo2 = [-1 for _ in range(n)]
        if n == 1:
            return nums[0]

        return max( self.dp(nums, 0, n-2, memo1), self.dp(nums, 1, n-1, memo2))
    
    def dp(self, nums:List[int], start:int, end:int, memo:List[int]):
        if start > end:
            return 0
        if memo[start] != -1:
            return memo[start]
        res = max( nums[start] + self.dp(nums, start +2, end , memo) , self.dp(nums, start+1, end, memo) )
        memo[start] = res
        return res
