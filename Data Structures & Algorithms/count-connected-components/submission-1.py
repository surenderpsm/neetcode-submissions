class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        visited = set()


        def dfs(node, prev):
            if node in visited: 
                return
            visited.add(node)
            for x in adj[node]:
                if x == prev:
                    continue
                dfs(x,node)



        res = 0

        for i in range(n):
            if i not in visited: 
                res+=1
                dfs(i,i-1)

        return res
            