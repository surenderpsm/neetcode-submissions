class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)

        for _, v in ctr.items():
            if v > 1:
                return True
        return False