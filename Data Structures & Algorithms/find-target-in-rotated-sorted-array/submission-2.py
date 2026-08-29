class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # at any arb mid, one side is sorted and the other isnt

        l,r = 0, len(nums)-1

        while l <= r:
            
            mid = (l+r)//2

            if nums[mid] == target:
                return mid


            if nums[mid]>=nums[l]:
                # left portion is sorted
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                    # check right portion
                # not in left at all
                else:
                    r = mid-1
            else:
                # right portion is sorted:
                if target < nums[mid] or target > nums[r]  :
                    r = mid -1
                else:
                    # should be in left
                    l = mid+1
        return -1