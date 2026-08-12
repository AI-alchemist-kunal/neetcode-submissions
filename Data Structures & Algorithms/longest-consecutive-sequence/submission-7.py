class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        sorted_list = sorted(set(nums))
        max_len = 1

        if len(nums) == 1:
            return max_len

        
        length = 1
        for i in range(len(sorted_list)-1):
        
            if sorted_list[i+1] == sorted_list[i]+1:
                length += 1
                max_len = max(max_len, length)
            elif sorted_list[i+1] != sorted_list[i]+1:
                length = 1
                max_len = max(max_len, length)

        return max_len


            
 