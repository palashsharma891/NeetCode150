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

# OR

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        str_set = set(s[l])
        max_len = 1

        while r < len(s):
            while s[r] in str_set:
                str_set.remove(s[l])
                l += 1
            str_set.add(s[r])
            r += 1
            max_len = max(max_len, len(str_set))

        return max_len
