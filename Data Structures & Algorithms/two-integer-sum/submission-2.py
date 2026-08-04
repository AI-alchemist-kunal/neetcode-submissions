class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) <= 1:
            return []
        # nums = sorted(nums)
        left = 0
        right = len(nums)-1
        result = []
        while len(nums) != 0:
            addition = nums[left] + nums[right]
            if addition == target:
                result.append(left)
                result.append(right)
                break
            elif addition < target:
                left = left + 1
            else:
                right = right - 1

        return result


        

        