class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        # till second last to be able to assign j and k
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            complement = -nums[i]
            while j < k:
                twosum = nums[j]+nums[k]
                if twosum == complement:
                    solution.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif twosum < complement:
                    j+=1
                else:
                    k-=1
        return solution



# sort it first

# -4, -1, -1, 0, 1, 2


# fix i; j and k are 2 pointers at two ends of subarray

# -4 : j(-1) k(2). 
# -1 : j(-1) k(2)

