class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we perform binary search to find the correct row where target might reside

        # we then use that rows bounds to find target again using binary search

        rows, cols = len(matrix), len(matrix[0])
        target_row = -1
        top, bottom = 0,rows-1
        while top <= bottom:
            mid = (top+bottom)//2



            if target < matrix[mid][0]:
                # target is smaller than the smallest elem in the row
                # then lower half including row is pruned
                bottom = mid-1
            elif target > matrix[mid][-1]:
                # target is larger than the last element of the row
                # then upper half including row is pruned
                top = mid+1
            else:
                # target is in this row
                target_row = mid
                break
        
        if target_row == -1:
            return False
        
        lo, hi = 0, cols-1

        while lo <= hi:
            mid = (lo+hi)//2

            if target < matrix[target_row][mid]:
                hi = mid-1
            elif target > matrix[target_row][mid]:
                lo = mid+1
            else:
                return True
        return False

        # mind = blow(mind)