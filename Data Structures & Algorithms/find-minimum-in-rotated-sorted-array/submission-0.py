class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we try to find the lower bound continously
        lo, hi = 0, len(nums)-1
        mid = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
                # all are unique elements so we dont need to handle equal case
        return nums[lo]
            