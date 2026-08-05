class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<= 0:
            return []
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]
            
            seen[num] = i
















        # if len(nums) <= 1:
        #     return []
        # seen = {}
        
        # for i, num in enumerate(nums):
        #     complement = target - num

        #     if complement in seen:
        #         return [seen[complement], i]
        #     seen[num] = i

    

        

        