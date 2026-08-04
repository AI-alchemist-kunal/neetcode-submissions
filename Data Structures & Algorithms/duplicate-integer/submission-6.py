class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # listt = self.nums
        hashmap = {}
        if not nums:
            return False

        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = True

        return False
        
        