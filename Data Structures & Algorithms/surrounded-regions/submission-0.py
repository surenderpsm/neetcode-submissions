class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        surrounded = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X':
                    surrounded[r][c] = 0
                elif r==0 or c==0 or r == ROWS-1 or c==COLS-1:
                    visited.add((r,c))
                    q.append((r,c))
                    surrounded[r][c] = 0
        while q:
            r,c = q.popleft()

            for dr, dc in directions:

                nr, nc = r+dr, c+dc

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited or board[nr][nc] == 'X':
                    continue
                surrounded[nr][nc] = 0
                visited.add((nr,nc))
                q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if surrounded[r][c]:
                    board[r][c] = 'X'
                



