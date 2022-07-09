class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        
        t_dict, window = {}, {}
        
        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)
            
        have, need = 0, len(t_dict)
        res, resLen = [-1, -1], float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in t_dict and window[c] == t_dict[c]:
                have += 1
                
            while have == need:
                #update our result
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                    
                #pop from left of window
                window[s[l]] -= 1
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -= 1
                    
                l += 1
                
        l, r = res
        return s[l:r+1]
