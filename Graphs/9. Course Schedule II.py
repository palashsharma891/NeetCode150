class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visiting, visited = set(), set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
                
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            visited.add(crs)
            preMap[crs] = []
            res.append(crs)
            return True
        
        res = []
        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return res
