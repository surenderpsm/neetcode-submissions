class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = "0"

            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    mr, mc = row + dr, col + dc
                    
                    if (mr < 0 or mc < 0 or mr >= ROWS or mc >= COLS or grid[mr][mc]=="0"):
                        continue
                    q.append((mr,mc))
                    grid[mr][mc] = "0"
        
        def dfs(r,c):
            s = collections.deque()
            grid[r][c] = "0"

            s.append((r,c))

            while s:
                row, col = s.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    grid[nr][nc] = "0"

                    s.append((nr,nc))





        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands+=1

        return islands

