class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we push point into heap as tuples with distance as the key
        # a max heap is used because we need it to maintain the top k closest points. 
        # so at any time, the top element in the heap is the k farthest point from the origin 

        # how do we handle poitns of same distance.
        # we need an identifier or someting. a fifo approach. if it came first, we prioritize that.

        def dist(x,y):
            return x**2 + y**2

        heap = []
        for i,p in enumerate(points):
            x,y = p
            d = dist(x,y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, i, p))
            elif heap[0][0] < d:
                heapq.heappushpop(heap,(-d, i, p))
        
        return [p for _,_i,p in heap]
            


