from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1sorted = sorted(s1)

        if len(s1) > len(s2):
            return False
        
        while r < len(s2):
            s2sorted = sorted(s2[l:r+1])
            if s1sorted == s2sorted:
                return True
            l += 1
            r += 1
        
        return False