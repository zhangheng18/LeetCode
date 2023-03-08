class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right  = 0 , len(numbers) -1
        while left < right:
            sum_val = numbers[left] + numbers[right]
            if sum_val < target:
                left +=1
            elif sum_val > target:
                right -=1
            else:
                return [left+1, right+1]
        return [-1,-1]
