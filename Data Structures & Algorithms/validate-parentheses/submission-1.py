class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        mapping = {")":"(", "}":"{", "]":"["}

        stack = []
        # s= "[({})]"

        for char in s:
            if char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack)==0
 


        