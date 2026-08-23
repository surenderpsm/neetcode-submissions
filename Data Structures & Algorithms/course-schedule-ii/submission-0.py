class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        order = []

        visit = set()
        completed = set()

        def dfs(crs):

            if not prereq[crs]: 
                if crs not in completed: 
                    order.append(crs)
                    completed.add(crs)
                return True

            if crs in visit: return False


            visit.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre): return False

            visit.remove(crs)
            prereq[crs] = []
            order.append(crs)
            completed.add(crs)
            return True

        

        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return order