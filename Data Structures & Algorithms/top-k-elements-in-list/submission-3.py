class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<= 1:
            return nums
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse = True)

        final = list(x[0] for x in sorted_freq[:k])

        return final

        
        

        