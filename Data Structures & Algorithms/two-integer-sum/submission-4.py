class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            map[n] = i

        for i,n in enumerate(nums):
            if target-n in map and map[target-n]!=i:
                return [i,map[target-n]] if i < map[target-n] else [map[target-n],i]
        return []