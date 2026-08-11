class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        sorted_nums = sorted(nums)
        longest = collections.defaultdict(set)

        for i in range(len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]+1:
                longest['l'].add(sorted_nums[i])
                longest['l'].add(sorted_nums[i-1])

        return len(longest['l'])