class Solution:

    def encode(self, strs: List[str]) -> str: 
        if not strs:
            return False
        strr = ""
        for ele in strs:
            strr += str(len(ele)) + "#" + ele
        return strr


    def decode(self, s: str) -> List[str]:
        if not s:
            return False
        result = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != "#"):
                j+=1
            length = int(s[i:j])

            start = j+1
            result.append(s[start:start+length])

            i = start + length

        return result

