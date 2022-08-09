class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        min_d = 0
        heapq.heapify(ans)
        for pt in points:
            d = pt[0]**2 + pt[1]**2
            heapq.heappush(ans, (-d, pt)) #always push
            if len(ans) > k: #pop when
                heapq.heappop(ans)
                
        return [y for x, y in ans]
      
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap += [[x**2 + y**2, x, y]]
        
        heapq.heapify(minHeap)
        
        res = []
        for i in range(k):
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            
        return res
