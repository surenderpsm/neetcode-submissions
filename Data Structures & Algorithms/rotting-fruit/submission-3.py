class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()

        visited = set()
        fresh = 0

        # collecting rotten fruit cells
        # also tracking fresh oranges
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        def add(r,c):
            if min(r,c)<0 or r==ROWS or  c == COLS or (r,c) in visited or grid[r][c] == 0:
                return
            grid[r][c] = 2
            nonlocal fresh
            fresh-=1
            visited.add((r,c))
            q.append((r,c))


        elapsed = 0
        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                add(r-1,c)
                add(r+1, c)
                add(r, c-1)
                add(r, c+1)
            elapsed+=1


        if not fresh: return elapsed

        return -1


        