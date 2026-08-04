class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # listt = self.nums
        hashmap = {}

        for i in nums:
            if i in hashmap.keys():
                return True
            else:
                hashmap[i]= hashmap.get(i, 0)+1
        for i in hashmap.keys():
            if hashmap[i] <= 1:
                return False
        
        