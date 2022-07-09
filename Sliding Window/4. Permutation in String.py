from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1ctr,  s2ctr = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            s1ctr[ord(s1[i]) - ord('a')] += 1
            s2ctr[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            matches += (1 if  s1ctr[i] == s2ctr[i] else 0)
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # for sliding the right end of the window
            index = ord(s2[r]) - ord('a') #find what character has been added to window
            s2ctr[index] += 1 #increment character's count in counter array
            if s1ctr[index] == s2ctr[index]: #if frequencies same
                matches += 1                 #then matches++
            elif s1ctr[index] + 1 == s2ctr[index]:#if frequency is increased in s2ctr after adding this new character
                matches -= 1                 #then matches--
                
            # for sliding left end of window
            index = ord(s2[l]) - ord('a') # find what character has been removed from window
            s2ctr[index] -= 1 # decrement the character's count in counter array
            if s1ctr[index] == s2ctr[index]: # if removing that character equals both counts
                matches += 1                 #mathces ++
            elif s1ctr[index] - 1 == s2ctr[index]: #if frequency is decrased in s2ctr after removing from left
                matches -= 1                      #matches--
                
            l += 1 #keep sliding the window
            
        return matches == 26
