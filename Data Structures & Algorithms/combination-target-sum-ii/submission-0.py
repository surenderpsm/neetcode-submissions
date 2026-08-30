class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort to reduce stack size (recursion)
        candidates.sort()

        # res stores the final list of lists
        res = []

        # helper for recursion. i current item index, cur array collected, total sum of cur array 
        def helper(i, cur, total):
            # found a combination
            if target == total:
                res.append(cur.copy())
                return 
            # out of bounds and total exceeded target, so we abandon this branch
            if total > target or i == len(candidates):
                return
            
            # append current item
            cur.append(candidates[i])
            helper(i+1, cur, total + candidates[i])
            cur.pop()

            # check for non unique candidates. easy cause its sorted
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            helper(i+1,cur, total)



        helper(0,[],0)
        return res
            