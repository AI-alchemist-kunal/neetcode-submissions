class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)<= 1:
            return [strs]

        groups = {}
        
        for string in strs:
            key = "".join(sorted(string))

            if key not in groups:
                groups[key] = []
            
            groups[key].append(string)
        
        return list(groups.values())


        