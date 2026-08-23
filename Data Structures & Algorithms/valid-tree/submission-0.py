class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        # lets start from 0

        visited = set()

        def dfs(node, prev):
            
            if not adj[node]:
                # no children. its a valid tree on its own.
                visited.add(node)
                return True

            # cycle detected.
            if node in visited:
                return False
            visited.add(node)
            for x in adj[node]:
                if x == prev: continue
                if not dfs(x, node):
                    return False
            
            return True



        if not dfs(0,-1): return False

        for i in range(n):
            if i not in visited:
                return False
        return True