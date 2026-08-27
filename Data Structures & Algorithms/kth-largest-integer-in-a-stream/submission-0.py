class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
    def add(self, val: int) -> int:
        self.nums.append(val)
        heap = []
        for num in self.nums:
            if len(heap) < self.k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heappushpop(heap, num)
        return heap[0]
