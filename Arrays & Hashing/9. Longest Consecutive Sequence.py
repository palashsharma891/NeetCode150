class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for n in nums:
            if n-1 not in numSet:
                # start of a sequence
                l = 1
                while n+l in numSet:
                    l += 1
                maxLen = max(maxLen, l)

        return maxLen
