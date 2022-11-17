class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj = collections.defaultdict(list)
        adj = {i:[] for i in range(1, n+1)}
        
        for u, v, w in times:
            adj[u].append([w, v])
            
        
        time = 0
        visited = set()
        minHeap = [[0, k]]
        
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in visited:
                continue
                
            visited.add(v)
            time = w#max(time, w)
            print(time)
            
            for w1, v1 in adj[v]:
                if v1 not in visited:
                    heapq.heappush(minHeap, [w+w1, v1])
                    
        return time if len(visited) == n else -1
