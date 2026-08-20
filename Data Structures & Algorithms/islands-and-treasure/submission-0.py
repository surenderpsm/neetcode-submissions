class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we start from treasure points and bfs outward

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))


        def add(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append((r,c))


        
        dist = 0
        # we collected all treasures in queue. now to bfs
        while q:
            # we have all the cells in level 0 (aka treasure chest) [initial state]
            # we use for loop for keep track of levels. we add all the subsequent level cells to the queue, but we know from initial len(q) the number of the cells in current level.
            
            for i in range(len(q)):
                r,c =  q.popleft()
                grid[r][c] = dist
                add(r+1,c)
                add(r-1,c)
                add(r, c+1)
                add(r, c-1)
            dist+=1




        # distance is incremented when the current level is over.




    