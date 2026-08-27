class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need a max heap where the top has heaviest stone

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            x,y = -heapq.heappop(stones), -heapq.heappop(stones)
            
            n = abs(x-y)
            if n:
                heapq.heappush(stones, -n)
        
        if stones:
            return -stones[0]
        return 0