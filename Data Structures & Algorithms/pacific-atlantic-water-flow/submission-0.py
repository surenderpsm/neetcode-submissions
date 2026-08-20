class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # multisource, but here we start with the edges.

        ROWS, COLS = len(heights), len(heights[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        atlantic = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        pacific = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or c==0:
                    q.append((r,c))
                    pacific[r][c] = 1
                    visited.add((r,c))

        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc)<0 or nr==ROWS or nc == COLS or (nr,nc) in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    pacific[nr][nc] = 1
                    q.append((nr,nc))
                    visited.add((nr,nc))

        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if r==ROWS-1 or c == COLS-1:
                    q.append((r,c))
                    atlantic[r][c] = 1
                    visited.add((r,c))
        
        
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc)<0 or nr==ROWS or nc == COLS or (nr,nc) in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    atlantic[nr][nc] = 1
                    q.append((nr,nc))
                    visited.add((nr,nc))


        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])

        return res