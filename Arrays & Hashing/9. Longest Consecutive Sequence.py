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

# OR more complex way getting TLE
# lesson learnt -> use n-1 to find start of sequence, not n-1!!!!!!!!!!!!!


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if len(nums) < 2:
            return len(nums)
        max_len = 1
        for n in nums:
            if n+1 in numSet:
                temp = n+1
                curr_len = 1
                while temp in numSet:
                    curr_len +=1
                    temp += 1
                max_len = max(max_len, curr_len)

        return max_len
