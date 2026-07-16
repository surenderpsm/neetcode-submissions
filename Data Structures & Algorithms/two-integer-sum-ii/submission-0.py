class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since its sorted, place 2 pointers. l and r at two ends.

        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l+=1
            elif sum > target:
                r-=1
            else:
                return [l+1,r+1]
        return [] 