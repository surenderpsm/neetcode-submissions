class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r  = 0, len(heights)-1 
        maxarea = 0
        while l < r:
            maxarea = max(maxarea, min(heights[l], heights[r])*(r-l))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return maxarea

# use 2 pointers l and r, compute and maximise area
