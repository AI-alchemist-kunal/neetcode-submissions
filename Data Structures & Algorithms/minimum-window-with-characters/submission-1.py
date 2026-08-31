class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or t:
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0)+ 1

        if len(s) < len(t):
            return ""

        
        