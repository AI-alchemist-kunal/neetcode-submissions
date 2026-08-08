class Solution:

    def encode(self, strs: List[str]) -> str: 
        if not strs:
            return False
        strr = "#".join(ele for ele in strs)
        return strr


    def decode(self, s: str) -> List[str]:
        if not s:
            return False
        result = s.split(sep = '#')
        return result
