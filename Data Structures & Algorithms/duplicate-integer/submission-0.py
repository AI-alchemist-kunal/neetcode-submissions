class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listt = self.nums
        hashmap = {}

        for i in listt:
            if i in hashmap.keys():
                return True
                break
            else:
                hashmap[i]= hashmap.get(i, 0)+1
            return False
        