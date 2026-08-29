class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low, hi = 0, len(nums)-1
        while low <= hi:
            mid = (low+hi)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            else:
                hi = mid - 1
        return -1
