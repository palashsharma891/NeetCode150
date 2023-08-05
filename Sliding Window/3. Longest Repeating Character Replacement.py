class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
                
        return res

# OR

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        res = 0
        maxf = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # maybe the newly added character is now the most frequent

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                # we don't have to decrement maxf because (windowlen-maxf) > k wouldn't be affected if
                # maxf is smaller. It will only be affected if maxf increases.

            res = max(res, r - l + 1)
            r += 1

        return res
