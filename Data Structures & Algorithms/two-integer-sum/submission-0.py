class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap to where you can find the position using the value. Then look for it by computing complement (target - num)

        map = {}
        for pos,num in enumerate(nums):
            if target-num in map:
                # we found a 2 sum pair. 
                return [map[target-num], pos]
            map[num] = pos
        return []