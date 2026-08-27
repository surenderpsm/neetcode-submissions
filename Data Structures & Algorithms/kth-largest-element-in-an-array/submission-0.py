class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap

        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h,n)
            elif h[0] < n:
                heapq.heappushpop(h,n)
        return h[0]