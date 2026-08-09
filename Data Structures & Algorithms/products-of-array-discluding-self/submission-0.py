class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(math.prod(nums[i+1:]))
            if i > 0:
                result.append(math.prod(nums[i+1:])*math.prod(nums[:i]))

        return result
        