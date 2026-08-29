class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        l, r = 0, len(nums)-1

        # find lower bound (aka pivot)
        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        print(l)
        res = find(0,l-1)
        return res if res != -1 else find(l, len(nums)-1)