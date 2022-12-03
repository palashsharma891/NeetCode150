class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = s // 2
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
