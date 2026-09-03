class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(i, x, y, visited):
            if i == len(word):
                return True

            if x == ROWS or y == COLS or x < 0 or y < 0:
                return False
            thiscell = 1 << (x * COLS + y)

            if visited & thiscell:
                return False 

            if board[x][y] == word[i]:
                # launch a search
                return (
                    backtrack(i + 1, x + 1, y, visited | thiscell)
                    or backtrack(i + 1, x, y + 1, visited | thiscell)
                    or backtrack(i + 1, x, y - 1, visited | thiscell)
                    or backtrack(i + 1, x - 1, y, visited | thiscell)
                )
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(0, i, j, 0):
                    return True
        return False
