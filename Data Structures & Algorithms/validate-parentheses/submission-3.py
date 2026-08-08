class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        # s = "[{}]"
        mapping = {"]":"[", "}":"{", ")":"("}
        stack = []

        for char in s:
            if char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0





        