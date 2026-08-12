class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        sorted_list = sorted(set(nums))

        max_len = 1
        length = 1
        for i in range(1, len(sorted_list)):
        
            if sorted_list[i] == sorted_list[i-1]+1:
                length += 1
                max_len = max(max_len, length)
            else:
                length = 1

        return max_len


            
 