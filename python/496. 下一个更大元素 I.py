class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        res_stack = {}
        # 单调栈 查找下一个最大元素
        for i in reversed(nums2):
            while stack and stack[-1] < i:
                stack.pop()

            # 结果记录hash表
            res_stack[i] = stack[-1] if stack else -1
            stack.append(i)

        # 获取nums1 的结果
        return [ res_stack[i] for i in nums1]