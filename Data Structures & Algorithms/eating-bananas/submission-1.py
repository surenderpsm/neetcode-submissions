class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # aiming for nlogm n is pile length and m is the max number of bannas in pile
        lo, hi = 1, max(piles)
        res = hi
        while lo <= hi:
            k = (lo+hi)//2

            
            hr = 0
            for p in piles:
                hr += math.ceil(float(p) / k)

            if hr <= h:
                # although valid solution we are minimizing
                res = k
                hi = k-1
            else:
                lo = k+1
        return res