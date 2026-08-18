class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        R,C = len(grid), len(grid[0])
        visited = set()
        maxarea = 0

        def dfs(row,col):
            area = 1
            s = deque()

            s.append((row,col))
            visited.add((row,col))
            while s:
                r,c = s.pop()
                directions = [(0,1), (0,-1), (-1,0), (1,0)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= R or nc >= C or grid[nr][nc] == 0 or (nr,nc) in visited:
                        continue
                    s.append((nr,nc))
                    visited.add((nr,nc))
                    area+=1

            return area

        for row in range(R):
            for col in range(C):
                if grid[row][col]:
                    maxarea = max(maxarea, dfs(row,col))
        return maxarea

