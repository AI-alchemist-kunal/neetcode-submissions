class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 0
        left = 0
        substr = set()

        for right in range(len(s)):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[right])

            max_len = max(max_len, len(substr))

        return max_len

        


         
        