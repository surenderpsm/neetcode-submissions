class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # compute frequency map. and print the top k keys of those frequencies

        # refresh: we use bucket sort to find the top k elements. we use the bucket criteria as the values. 

        map = Counter(nums)

        # for the bucket, we do the size of the array becuse max frequency is the size of the array.

        # how do we create the bucket? we need dictionary, which holds list of values in list. 

        # 1->[], 2-> [] ... n -> []

        # run a for loop over map and build the bucket
        bucket = defaultdict(list)
        for num, freq in map.items():
            bucket[freq].append(num)
            # each number is segregated by frequency

        # now from highest frequncy to lowest, we run a for loop and append to solution until solution is size k
        sol = []

        for freq in range(len(nums), 0, -1):
            if freq in bucket:
                sol.extend(bucket[freq])
                if len(sol) == k:
                    break
        return sol
        
        
# consolidation

# use frequency as the criteria to segregate into buckets.
# pick the top k elements by going through bucket in decending order of frequecny

