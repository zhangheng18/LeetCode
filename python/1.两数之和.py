class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2index = {}
        for idx,num in enumerate(nums):
            need = target - num
            if need in value2index:
                return [idx,  value2index[need]]
            value2index[num] = idx
        return []
