class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        required = len(need)

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # This character requirement is now satisfied
            if char in need and window[char] == need[char]:
                have += 1

            # Current window contains everything we need
            while have == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # Window is no longer satisfying this requirement
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result