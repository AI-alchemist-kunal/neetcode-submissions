class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 0
        left = 0

        substr = [s[left]]
        length = len(substr)
        max_len = max(length, max_len)

        for right in range(1, len(s)):
            if s[right] not in substr:
                substr.append(s[right])
                length = len(substr)
                max_len = max(length, max_len)

            else:
                left+=1
                substr =[s[left]]

            # length = len(substr)
            # max_len = max(length, max_len)

        return max_len

        


         
        