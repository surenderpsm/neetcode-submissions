class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()

        nums_set.update(nums)
        maxlen = 0
        for num in nums_set:
            if num-1 not in nums_set:
                # start of sequence
                seq = 0
                curr = num
                while curr in nums_set:
                    seq+=1
                    curr+=1
                maxlen = max(maxlen, seq)
        return maxlen