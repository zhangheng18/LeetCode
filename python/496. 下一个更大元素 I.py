class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def next_max_element(nums):
            # 查找下一个最大元组
            stack = []
            res = [-1] * len(nums)
            for i in range(len(nums)):
                while stack and nums[stack[-1]]< nums[i]:
                    res[stack.pop()] = nums[i]
                stack.append(i)
            return res
        # nums2 元素字典映射
        next_nums2 = next_max_element(nums2)
        next_dic = { nums2[i]:next_nums2[i] for i in range(len(nums2))}

        # nums1 最大元素
        ans = []
        for num in nums1:
            ans.append( next_dic[num])
        return ans