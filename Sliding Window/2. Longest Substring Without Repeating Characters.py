class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_len = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in d and l <= d[s[r]]:
                l = d[s[r]] + 1
            else: 
                max_len = max(max_len, r - l + 1)
            d[s[r]] = r
            
        return max_len
