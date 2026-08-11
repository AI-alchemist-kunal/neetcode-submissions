class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        sorted_nums = sorted(nums)
        uniq_nums = list(set(sorted_nums))
        longest = collections.defaultdict(set)
        if len(uniq_nums)==1:
            return 1
        else:
            for i in range(len(uniq_nums)):
                if uniq_nums[i] == uniq_nums[i-1]+1:
                    longest['l'].add(uniq_nums[i-1])
                    longest['l'].add(uniq_nums[i])

        return len(longest['l'])