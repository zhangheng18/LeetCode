import heapq


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 田忌赛马

        # nums1 升序排序
        nums1.sort()

        # 构建 降序堆
        nums2_heap = [(-val, i) for i, val in enumerate(nums2)]
        heapq.heapify(nums2_heap)

        left, right = 0, len(nums2) - 1

        res = [0] * len(nums2)
        while nums2_heap:
            val, i = heapq.heappop(nums2_heap)
            val = -val

            if val < nums1[right]:
                # nums1 大
                res[i] = nums1[right]
                right -= 1
            else:
                # nums1 小
                res[i] = nums1[left]
                left += 1
        return res
