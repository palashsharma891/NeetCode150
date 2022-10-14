class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {src:[] for src, dest in tickets}
        
        tickets.sort()
        for src, dest in tickets:
            adjList[src].append(dest)
            
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for v in temp:
                res.append(v)
                adjList[src].pop(0)
                if dfs(v):
                    return True
                res.pop()
                adjList[src].append(v)
                    
            return False
            
        dfs('JFK')
        return res
