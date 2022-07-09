class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        
        for r, n in enumerate(nums):
            
            while q and nums[q[-1]] <= n:
                q.pop()
            q.append(r)
            
            # remove 1st element if it is outside the window
            if r - q[0] == k:
                q.popleft()
                
            # if window has k elements, add to results. this is invalid only for first k elements
            if r + 1 >= k:
                res.append(nums[q[0]])
                
        return res
