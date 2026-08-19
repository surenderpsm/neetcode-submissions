class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        area = 0
        
        def dfs(row, col) -> int:
            s = deque()

            directions = [[0,1], [1,0], [-1,0], [0,-1]]

            s.append((row, col))
            a = 1
            grid[row][col] = 0
            while s: 
                r,c = s.pop()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if nr<0 or nc<0 or nr>=ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    a+=1
                    s.append((nr,nc))
            return a           


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        return area