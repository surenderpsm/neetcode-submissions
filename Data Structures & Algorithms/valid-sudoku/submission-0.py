class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9
        rows = [0] * 9
        boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                else:
                    curr = 1 << int(board[row][col])
                box_index = (row//3)*3 + (col//3)

                if rows[row] & curr or columns[col] & curr or boxes[box_index] & curr:
                    return False
                
                
                rows[row] |= curr
                columns[col] |= curr
                boxes[box_index] |= curr
        return True

        
