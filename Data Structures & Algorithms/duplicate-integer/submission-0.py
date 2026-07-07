class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a hashmap and store the frequencies of the array.

        map = defaultdict(int)

        for num in nums:
            map[num]+=1

        max = 0
        for v in map.values():
            if v != 1:
                return True
        return False
