class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or t:
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0)+ 1

        if len(s) < len(t):
            return ""

        left = 0
        max_len = 0
        length = 0

        for right in range(len(s)):
            if s[right] in t:
                length+=1
                max_len = max(length, max_len)
            else: 
                break

        return max_len
                



        
        