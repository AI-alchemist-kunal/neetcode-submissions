class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        

        if s == s[::-1]:
            return True
        else:
            return False
        

        