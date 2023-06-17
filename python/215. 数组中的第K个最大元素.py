import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            # 保持堆的大小为k
            heapq.heappush(pq, i)
            if len(pq) > k:
                heapq.heappop(pq)
        # 堆顶是最小的那个，即第 k 个最大元素
        return pq[0]