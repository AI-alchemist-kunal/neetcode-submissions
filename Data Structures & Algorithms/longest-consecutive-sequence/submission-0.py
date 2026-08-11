class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        sorted_nums = sorted(nums)
        uniq_nums = set(sorted_nums)
        length = len(uniq_nums)

        return length