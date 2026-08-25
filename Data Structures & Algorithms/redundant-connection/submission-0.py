class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        def find(n):
            if n!=parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union (a,b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False
            

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2]+=1
            return True


        for a,b in edges:
            if not union(a,b):
                return [a,b]